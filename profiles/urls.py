from django.urls import path
from .views import UserProfileView, CraftsmanProfileView, ProfileRedirectView

urlpatterns = [
    path('profile/', ProfileRedirectView.as_view(), name='profile'),
    path("user/", UserProfileView.as_view(), name="user_profile"),
    path("cratsman/", CraftsmanProfileView.as_view(), name="craftsman_profile"),
]