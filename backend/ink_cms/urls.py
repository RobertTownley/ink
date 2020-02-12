from django.urls import include, path

from ink_cms.api import router
from ink_cms.views import ImageUploadView

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("image_upload/", ImageUploadView.as_view()),
]
