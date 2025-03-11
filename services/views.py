from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Service
from .forms import ServiceForm
from django.db.models import Q

# Create your views here.
class ServiceListView(ListView): # display all services in the database
    model = Service
    template_name = "services/service_list.html"
    context_object_name = "services"
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
            )
        return queryset

class ServiceDetailView(DetailView): # display only one service and all craftsmen doing this service
    model = Service
    template_name = "services/service_detail.html"
    context_object_name = "service"

class ServiceCreateView(PermissionRequiredMixin, CreateView): # this is for admin
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_create.html'
    success_url = reverse_lazy('service_list')
    permission_required = 'services.can_create_service'

    def handle_no_permission(self):
        messages.error(self.request, 'You do not have permission to create services.')
        return super().handle_no_permission()
