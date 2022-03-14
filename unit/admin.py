# # Register your models here.

import imp
from nturl2path import url2pathname
from django.contrib import admin
from .models import Post, Category, Tag, MyUser,Comments
from django.utils.html import format_html
from django.urls import reverse
import csv
from django.http import HttpResponse

class PostAdmin(admin.ModelAdmin):
    def photo(self,object):
        return format_html(f"<img src='{object.featured_image.url}' width='40' style='border-radius:50px' />")

    list_display=['id','photo','title','author','category','created_date']
    list_display_links=['id','photo','title']
    search_fields=['category','tag']
    list_filter=['category','tag','created_date','author']
    filter_horizontal = ['tag']

    def view_on_site(self,obj):
        url = reverse('post_detail', kwargs={'pk':obj.pk})
        return url 
class MyUserAdmin(admin.ModelAdmin):
    actions = ['export_as_csv']
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(["first_name","last_name","email","about"])
        for obj in queryset:
            # row = writer.writerow([getattr(obj, field) for field in field_names])
            row = writer.writerow([obj.first_name,obj.last_name,obj.email,obj.about])
        return response
    export_as_csv.short_description = "Export Selected"

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(MyUser,MyUserAdmin)
admin.site.register(Comments)


