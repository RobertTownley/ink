from rest_framework import routers

from ink_cms.config import INK_CONFIG
from ink_cms.views import (
    ArticleViewSet,
    BlogEntryViewSet,
    PageViewSet,
    RevisionViewSet,
    StaffViewSet,
    SiteSectionViewSet,
    TagViewSet,
)

router = routers.DefaultRouter()
router.register("revisions", RevisionViewSet)
router.register("staff", StaffViewSet)
router.register("site_sections", SiteSectionViewSet)
router.register("tags", TagViewSet)

API_MAPPINGS = {
    "ink_cms.Article": {"endpoint": "articles", "viewset": ArticleViewSet},
    "ink_cms.BlogEntry": {"endpoint": "blogentries", "viewset": BlogEntryViewSet},
    "ink_cms.Page": {"endpoint": "pages", "viewset": PageViewSet},
}

for model_name in INK_CONFIG["CONTENT_MODELS"]:
    api_entry = API_MAPPINGS[model_name]
    router.register(api_entry["endpoint"], api_entry["viewset"])
