from django.contrib import admin
from core.models import Question, Choice, Person
from django.utils import timezone
import datetime
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        
        'question_text',
        'pub_date',
        'was_published_recently',
    ]
    # fields = [
    #     'pub_date',
    #     'question_text'
    # ]
    fieldsets = [
        ("The Question", {'fields': ['question_text']}),
        ("Meta Data", {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]
    search_fields = ["question_text"]
    list_filter = ["pub_date"]

    

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Person)