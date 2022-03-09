# Register your models here.
from django.contrib import admin

from .models import Question, Choice




# # admin.site.register(Question, QuestionAdmin)

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]



admin.site.register(Choice)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
# class ChoiceInline(admin.TabularInline):

admin.site.register(Question, QuestionAdmin)