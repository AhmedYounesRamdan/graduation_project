from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View

# Create your views here.
class HomepageView(TemplateView):
    template_name = "pages/home.html"

class AboutpageView(TemplateView):
    template_name = "pages/about.html"

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "pages/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_craftsman:
            context["user_type"] = "Craftsman"
        else:
            context["user_type"] = "Customer"
        return context