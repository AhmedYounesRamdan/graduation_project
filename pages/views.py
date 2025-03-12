from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, UpdateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth import get_user_model
from craftsmen.models import Craftsman
from django.shortcuts import get_object_or_404
from .forms import UserProfileUpdateForm, CraftsmanProfileUpdateForm

CustomUser = get_user_model()

# Create your views here.
class HomepageView(TemplateView):
    template_name = "pages/home.html"

class AboutpageView(TemplateView):
    template_name = "pages/about.html"

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if hasattr(request.user, 'craftsman'):
            return redirect('craftsman_profile')
        else:
            return redirect('user_profile')

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "pages/profiles/user_profile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Pass the logged-in user to the template
        return context

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserProfileUpdateForm
    template_name = "pages/profiles/user_profile_update.html"
    success_url = reverse_lazy('user_profile')

    def get_object(self):
        return self.request.user
    
class CraftsmanProfileView(LoginRequiredMixin, TemplateView):
    template_name = "pages/profiles/craftsman_profile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fetch the craftsman profile for the logged-in user
        craftsman = get_object_or_404(Craftsman, user=self.request.user)
        context['craftsman'] = craftsman
        
        return context
    
class CraftsmanProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Craftsman
    form_class = CraftsmanProfileUpdateForm
    template_name = "pages/profiles/craftsman_profile_update.html"
    success_url = reverse_lazy('craftsman_profile')

    def get_object(self):
        return self.request.user.craftsman
    