from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from ink_cms.views import BlogEntryDetailView, BlogEntryListView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("ink/", include("ink_cms.urls")),
    path("blog/", BlogEntryListView.as_view()),
    path("blog/<slug:slug>/", BlogEntryDetailView.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
