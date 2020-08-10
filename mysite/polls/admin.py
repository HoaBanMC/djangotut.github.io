from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets= [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    #sap xep list cac question theo danh sach
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    #sap xep tim theo thoi gian
    list_filter = ['pub_date']
    #tao thanh tim kiem theo question
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)