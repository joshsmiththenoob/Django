from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home, name = "home"),
    path("<int:id>/", views.post, name= "post") # only receive integer value of path variable id
]

