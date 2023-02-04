from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"), # main page = fill out a form with necessary info + images
    path("laptopUpload", views.laptopUpload, name="laptopUpload"),
    path("desktopUpload", views.desktopUpload, name="desktopUpload"),
    path("cameraUpload", views.cameraUpload, name="cameraUpload"),
    path("result", views.result, name="result"),
    path("about", views.about, name="about")
]