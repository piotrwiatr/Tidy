from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"), # main page = fill out a form with necessary info + images
    path("about", views.about, name="about")
                                         # request page that redirects to review page, does the necessary stuff.
                                         # review page = check what the AI has suggested and choose whether to upload to kijiji
]