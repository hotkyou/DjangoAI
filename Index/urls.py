from django.urls import include, path

from . import views

app_name = "Index"

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.index, name="identification-documents"),
    path("", views.index, name="driver-license"),
    path("", views.index, name="report-card"),
]