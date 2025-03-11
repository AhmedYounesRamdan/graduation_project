from django.urls import path
from .views import HomepageView, AboutpageView, DashboardView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

urlpatterns = [
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("about/", AboutpageView.as_view(), name="about"),
    path("", HomepageView.as_view(), name="home"),
]