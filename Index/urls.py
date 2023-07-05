from django.urls import include, path

from . import views

app_name = "Index"

urlpatterns = [
    path("", views.index, name="index"),
]