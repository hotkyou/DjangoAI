from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("diagnose/", include("diagnose.urls")),
    path("CharacterRecoAI/", include("CharacterRecoAI.urls")),
    path("FaceRecoAI/", include("FaceRecoAI.urls")),
    path("admin/", admin.site.urls),
    path("", include("Index.urls")),
]
