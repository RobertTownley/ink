import json

from django.apps import apps
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.forms.models import ModelForm
from django.http import JsonResponse

from ink_cms.actions import (
    handle_revert,
    handle_save,
    handle_publication,
    handle_unpublication,
)
from ink_cms.config import INK_CONFIG
from ink_cms.errors import no_revision_found
from ink_cms.forms import ArticleForm, BlogEntryForm, PageForm
from ink_cms.models import Revision, SiteSection


class InkAdmin(admin.ModelAdmin):
    change_form_template = "ink_cms/admin.html"
    list_display = ["id", "title", "publication_date", "slug"]
    list_display_links = ["id", "title"]
    list_filter = ["publication_date"]

    def __init__(self, model, site, **kwargs):
        if self.form == ModelForm:
            # Form wasn't changed by user; use Ink defaults
            INK_FORMS = {
                "Article": ArticleForm,
                "BlogEntry": BlogEntryForm,
                "Page": PageForm,
            }
            self.form = INK_FORMS[model.__name__]
        return super().__init__(model, site, **kwargs)

    def _changeform_view(self, request, object_id, form_url, extra_context):
        if request.method == "POST":
            data = json.loads(request.body)
            action = data.get("_cms_action")
            change = bool(object_id)
            if change:
                obj = self.get_object(request, object_id)
            else:
                if not self.has_add_permission(request):
                    raise PermissionDenied
                obj = None
            if action:
                del data["_cms_action"]
            if action == "save":
                ModelForm = self.get_form(request, change=change)
                form = ModelForm(data, request.FILES, instance=obj)
                return handle_save(change, data, form, request)
            elif action == "revert":
                return handle_revert(data, object_id, request)
            elif action == "publish":
                ModelForm = self.get_form(request, change=change)
                form = ModelForm(data, request.FILES, instance=obj)
                return handle_publication(data, form, request)
            elif action == "unpublish":
                return handle_unpublication(obj)

        elif request.method == "GET" and request.GET.get("format") == "json":
            content_type = ContentType.objects.get_for_model(self.model)
            latest = (
                Revision.objects.filter(object_id=object_id, content_type=content_type)
                .order_by("-date_created")
                .first()
            )
            if not latest:
                return no_revision_found()

            return JsonResponse(latest.data)

        extra_context = extra_context or {}
        extra_context["INK_DEV"] = INK_CONFIG["DEV"]
        return super()._changeform_view(request, object_id, form_url, extra_context)


for model_name in INK_CONFIG["CONTENT_MODELS"]:
    model = apps.get_model(model_name)
    admin.site.register(model, InkAdmin)

# Support models
@admin.register(SiteSection)
class SiteSectionAdmin(admin.ModelAdmin):
    pass
