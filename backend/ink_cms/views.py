import json

from django.apps import apps
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.http import Http404, JsonResponse
from django.views.generic import DetailView, ListView, View
from rest_framework.permissions import (
    DjangoModelPermissions,
    DjangoModelPermissionsOrAnonReadOnly,
)
from rest_framework import viewsets

from ink_cms.config import INK_CONFIG
from ink_cms.pagination import InkPagination
from ink_cms.serializers import ImageSerializer
from ink_cms.models import (
    Article,
    BlogEntry,
    Page,
    Revision,
    SiteSection,
    Tag,
    UploadedImage,
)
from ink_cms.serializers import (
    ArticleSerializer,
    ArticleListSerializer,
    BlogEntrySerializer,
    BlogEntryListSerializer,
    PageSerializer,
    PageListSerializer,
    RevisionSerializer,
    StaffSerializer,
    SiteSectionSerializer,
    TagSerializer,
)


class AbstractInkViewSet(viewsets.ModelViewSet):
    lookup_field = "slug"
    pagination_class = InkPagination
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_serializer_class(self):
        if getattr(self, "action", None) == "list" and hasattr(
            self, "serializer_list_class"
        ):
            return self.serializer_list_class
        else:
            return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        if self.request.GET.get("tag"):
            tag = self.request.GET["tag"]
            qs = qs.filter(tags__name=tag)
        if self.request.GET.get("topic"):
            site_section_id = int(self.request.GET.get("topic"))
            qs = qs.filter(site_section_id=site_section_id)
        return qs


class ArticleViewSet(AbstractInkViewSet):
    queryset = Article.objects.filter(workflowstate="Published")
    serializer_class = ArticleSerializer
    serializer_list_class = ArticleListSerializer


class BlogEntryViewSet(AbstractInkViewSet):
    queryset = BlogEntry.objects.filter(workflowstate="Published")
    serializer_class = BlogEntrySerializer
    serializer_list_class = BlogEntryListSerializer


class PageViewSet(AbstractInkViewSet):
    queryset = Page.objects.filter(workflowstate="Published")
    serializer_class = PageSerializer
    serializer_list_class = PageListSerializer


class RevisionViewSet(viewsets.ModelViewSet):
    pagination_class = InkPagination
    permission_classes = [DjangoModelPermissions]
    serializer_class = RevisionSerializer
    queryset = Revision.objects.all().select_related("user")

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        if self.request.GET.get("modelName") and self.request.GET.get("appName"):
            app_name = self.request.GET.get("appName")
            model_name = self.request.GET.get("modelName")
            Model = apps.get_model(f"{app_name}.{model_name}")
            content_type = ContentType.objects.get_for_model(Model)
            qs = qs.filter(content_type=content_type)
        if self.request.GET.get("id"):
            object_id = int(self.request.GET.get("id"))
            qs = qs.filter(object_id=object_id)
        return qs


class StaffViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.filter(is_active=True, is_staff=True)
    serializer_class = StaffSerializer


class SiteSectionViewSet(viewsets.ModelViewSet):
    queryset = SiteSection.objects.all()
    serializer_class = SiteSectionSerializer


class TagViewSet(viewsets.ModelViewSet):
    # TODO: Save tags on publication (or save?)
    #
    # Context: These tags aren't currently saved to Tag models
    # on publication, so the Tag object is never created. Once these models
    # are created, the frontend will start including them in the Tags content panel.
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ImageUploadView(View):
    def post(self, request):
        model_name = request.POST.get("model_name")
        Model = apps.get_model(model_name)
        try:
            obj = Model.objects.get(id=int(request.POST.get("object_id")))
        except Model.DoesNotExist:
            raise Http404()

        # Image Block
        upload = UploadedImage.objects.create(obj=obj)
        upload.image = request.FILES["uploaded_file"]
        upload.save()
        data = ImageSerializer(upload.image).data
        return JsonResponse(data)


class DetailViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["frontend_context"] = json.dumps(INK_CONFIG["FRONTEND_CONTEXT"])
        context["object_data"] = self.serializer_class(context["object"]).data
        context["INK_DEV"] = INK_CONFIG["DEV"]
        return context


class ListViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["frontend_context"] = json.dumps(INK_CONFIG["FRONTEND_CONTEXT"])
        context["INK_DEV"] = INK_CONFIG["DEV"]
        return context


class BlogEntryListView(ListViewMixin, ListView):
    model = BlogEntry
    queryset = BlogEntry.objects.filter(workflowstate="Published")
    serializer_class = BlogEntrySerializer
    template_name = "ink_cms/blogentry_list.html"


class BlogEntryDetailView(DetailViewMixin, DetailView):
    lookup_field = "slug"
    model = BlogEntry
    serializer_class = BlogEntrySerializer
    template_name = "ink_cms/blogentry_detail.html"
