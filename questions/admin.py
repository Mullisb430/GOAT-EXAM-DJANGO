from django.contrib import admin
from .models import Questions

class QuestionsAdmin(admin.ModelAdmin):
    fields = ['question', 'answer_one', 'answer_two', 'answer_three', 'answer_four', 'skills']
    list_display = ('question', 'answer_one', 'answer_two', 'answer_three', 'answer_four', 'skills')    
    search_fields = ['question', 'answer_one', 'answer_two', 'answer_three', 'answer_four', 'skills']

admin.site.register(Questions, QuestionsAdmin)

