from django.contrib import admin
from django.contrib import admin
from .models import Blog,Category,DoctorInfo
# Register your models here.

admin.site.register(Blog)
admin.site.register(DoctorInfo)
admin.site.register(Category)