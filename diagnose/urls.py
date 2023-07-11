from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.diagnose, name="disgnose"),
]