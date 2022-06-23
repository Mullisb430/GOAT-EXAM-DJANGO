from django.contrib import admin
from .models import Questions

class QuestionsAdmin(admin.ModelAdmin):
    fields = ['question', 'answer_one', 'answer_two', 'answer_three', 'answer_four']
    list_display = ('question', 'answer_one', 'answer_two', 'answer_three', 'answer_four')    
    search_fields = ['question', 'answer_one', 'answer_two', 'answer_three', 'answer_four']

admin.site.register(Questions, QuestionsAdmin)

