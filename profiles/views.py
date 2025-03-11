from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, TemplateView
from profiles.models import UserProfile
from .forms import UserProfileForm
from django.views import View

class ProfileRedirectView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if hasattr(request.user, 'craftsman'):  # Check if the user has a Craftsman profile
            return redirect('craftsman_profile')  # Redirect to craftsman profile
        else:
            return redirect('user_profile')  # Redirect to regular user profile

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/user_profile/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.userprofile
        return context

class CraftsmanProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/craftsman_profile/profile_detail.html'
    
# class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = UserProfile
#     form_class = UserProfileForm
#     template_name = 'accounts/user_profile_form.html'

#     def get_object(self):
#         return self.request.user.userprofile

#     def get_success_url(self):
#         return reverse('user_profile')