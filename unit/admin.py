# Register your models here.

from django.contrib import admin
from django.test import tag
from .models import Post,Category,Tag,MyUser

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(MyUser)




