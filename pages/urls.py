from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

urlpatterns = [
    path("about/", views.AboutpageView.as_view(), name="about"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("user_profile/", views.UserProfileView.as_view(), name="user_profile"),
    path("user_profile/update/", views.UserProfileUpdateView.as_view(), name="user_profile_update"),
    path("craftsman_profile/", views.CraftsmanProfileView.as_view(), name="craftsman_profile"),
    path("craftsman_profile/update/", views.CraftsmanProfileUpdateView.as_view(), name="craftsman_profile_update"),
    path("", views.HomepageView.as_view(), name="home"),
]