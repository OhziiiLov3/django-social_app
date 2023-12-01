from django.urls import path
from .views import dashboard , profile_list, profile_detail

app_name = "main_app"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile_detail/<int:pk>", profile_detail , name="profile_detail"),
]