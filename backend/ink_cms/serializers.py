import os

from django.conf import settings
from django.contrib.auth import get_user_model
from easy_thumbnails.files import get_thumbnailer
from rest_framework import serializers

from ink_cms.config import INK_CONFIG
from ink_cms.models import Article, BlogEntry, Page, Revision, SiteSection, Tag


class SharedTaxonomySerializer(serializers.ModelSerializer):
    pass


class SiteSectionSerializer(SharedTaxonomySerializer):
    class Meta:
        fields = "__all__"
        model = SiteSection


class TagSerializer(SharedTaxonomySerializer):
    class Meta:
        fields = "__all__"
        model = Tag


class StaffSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()

    class Meta:
        exclude = [
            "date_joined",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "last_login",
            "password",
            "user_permissions",
        ]
        model = get_user_model()

    def get_display_name(self, obj):
        return getattr(obj, INK_CONFIG["USERNAME_DISPLAY"])()


class RevisionSerializer(serializers.ModelSerializer):
    user = StaffSerializer(read_only=True)

    class Meta:
        fields = "__all__"
        model = Revision


class LimitedRevisionSerializer(RevisionSerializer):
    user = None

    class Meta:
        exclude = ["action", "content_type", "date_created", "id", "object_id", "user"]
        model = Revision


class AbstractInkSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    site_section = SiteSectionSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        exclude = [
            "created_by",
            "creation_date",
            "id",
            "published_revision",
            "title",
            "workflowstate",
        ]

    def get_content(self, obj):
        return obj.published_revision.data if obj.published_revision else {}


class ListMixin:
    def get_content(self, obj):
        data = super().get_content(obj)
        list_fields = INK_CONFIG["LIST_FIELDS"]
        if list_fields == ["*"]:
            return data
        return {k: v for k, v in data.items() if k in list_fields}


class ArticleSerializer(AbstractInkSerializer):
    class Meta:
        exclude = AbstractInkSerializer.Meta.exclude
        model = Article


class ArticleListSerializer(ListMixin, ArticleSerializer):
    pass


class BlogEntrySerializer(AbstractInkSerializer):
    class Meta:
        exclude = AbstractInkSerializer.Meta.exclude
        model = BlogEntry


class BlogEntryListSerializer(ListMixin, BlogEntrySerializer):
    pass


class PageSerializer(AbstractInkSerializer):
    class Meta:
        exclude = AbstractInkSerializer.Meta.exclude
        model = Page


class PageListSerializer(ListMixin, PageSerializer):
    pass


class ImageSerializer(serializers.Serializer):
    filename = serializers.SerializerMethodField()
    optimized = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()

    def photo_option(self, obj, option_name):
        if not obj:
            return None
        option = INK_CONFIG["THUMBNAIL_ALIASES"][""][option_name]
        filepath = get_thumbnailer(obj).get_thumbnail(option).url
        return os.path.join(settings.MEDIA_URL, filepath)

    def get_filename(self, obj):
        return obj.name.rsplit("/", 1)[1]

    def get_optimized(self, obj):
        return self.photo_option(obj, "optimized")

    def get_thumbnail(self, obj):
        return self.photo_option(obj, "thumbnail")
