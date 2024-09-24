from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=55, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True) 
    def get_absolute_url(self):
        return reverse('profile_detail', args=[str(self.id)])