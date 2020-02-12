from django import forms
from django.utils.text import slugify

from ink_cms.models import Article, BlogEntry, Page


class SharedInkForm(forms.ModelForm):
    class Meta:
        exclude = ["published_revision", "tags", "workflowstate"]

    def clean(self, *args, **kwargs):
        slug = slugify(self.data.get("slug", "") or self.data.get("title", ""))
        self.data["slug"] = slug
        self.cleaned_data["slug"] = slug
        if self.errors.get("slug") and slug:
            del self.errors["slug"]
        super().clean(*args, **kwargs)


class ArticleForm(SharedInkForm):
    class Meta:
        exclude = SharedInkForm.Meta.exclude
        model = Article


class BlogEntryForm(SharedInkForm):
    class Meta:
        exclude = SharedInkForm.Meta.exclude
        model = BlogEntry


class PageForm(SharedInkForm):
    class Meta:
        exclude = SharedInkForm.Meta.exclude
        model = Page
