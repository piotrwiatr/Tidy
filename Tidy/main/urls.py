from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"), # main page = fill out a form with necessary info + images
    path("laptopUpload", views.laptopUpload, name="laptopUpload"),
    path("desktopUpload",views.desktopUpload, name="desktopUpload"),
    path("cameraUpload",views.cameraUpload, name="cameraUpload"),
    path("about", views.about, name="about")
                                         # request page that redirects to review page, does the necessary stuff.
                                         # review page = check what the AI has suggested and choose whether to upload to kijiji
]