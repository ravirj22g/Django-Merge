# Create your models here.

from django.conf import settings
from django.db.models.deletion import PROTECT
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    email = models.EmailField()
    phone = models.IntegerField(null=True, blank=True)
    # image = models.ImageField(null=True, blank=True, upload_to='users/')
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    about = models.TextField()
    designation = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=100)
    # slug = AutoSlugField(populate_from='name', max_length=200,editable=False)
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    # slug = AutoSlugField(populate_from='name', max_length=200,editable=False)
    def __str__(self):
        return self.name    

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=PROTECT,null=True,blank=True)
    tag = models.ManyToManyField(Tag)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True) 
    thumbnail_image = models.ImageField(upload_to='image/')  
    featured_image = models.ImageField(upload_to='image/')
    
      

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

