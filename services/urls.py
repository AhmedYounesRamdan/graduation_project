from django.urls import path
from .views import ServiceListView, ServiceDetailView, ServiceCreateView

urlpatterns = [
    path("", ServiceListView.as_view(), name="service_list"),
    path("<uuid:pk>/", ServiceDetailView.as_view(), name="service_detail"),
    path("create/", ServiceCreateView.as_view(), name="service_create"),
]