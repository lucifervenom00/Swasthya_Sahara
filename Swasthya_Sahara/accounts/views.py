from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin



from .models import CustomUser
from .forms import CustomUserUpdateForm

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"
    context_object_name = 'user'

    def get_user(self):
        return self.request.user
    
  


    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'account/User_update_view.html'

    def get_success_url(self):
        return reverse('profile')