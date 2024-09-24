from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse
from django.conf import settings
# Create your models here
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_absolute_url(self):    
        return reverse('home', args=[str(self.id)])
    
class Blog(models.Model):
    cover_img=models.ImageField(upload_to='images/',null=True,blank=True)
    title = models.CharField(max_length=100)
    content=CKEditor5Field()
    created_on = models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    category=models.CharField(max_length=100,default='Self-Care')
    def __str__(self):
        return self.title
    def get_absolute_url(self):    
        return reverse('blog_list', args=[str(self.id)])

    
class JournalEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "Journal Entries"


class DoctorInfo(models.Model):
    image=models.ImageField(upload_to='images/doctors/',null=True,blank=True)
    name=models.CharField(max_length=100)
    specialist=models.CharField(max_length=20,default='Psychiatric',null=False,blank=False)
    phone=models.CharField(max_length=10)
    email=models.EmailField(null=False,blank=False)
    address=models.TextField()
    class gender(models.TextChoices):
        Male="M","Male"
        Female="F","Female"
    gender=models.CharField(max_length=1,choices=gender.choices,null=False,blank=False)
    age=models.PositiveIntegerField(null=False,blank=False)
    def __str__(self):
        return self.name
    def get_absolute_url(self):    
        return reverse('doctor-list', args=[str(self.id)])