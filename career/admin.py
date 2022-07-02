from django.contrib import admin
from .models import Career

class CareerAdmin(admin.ModelAdmin):
    fields = ['name', 'special', 'skills']
    list_display = ('name', 'special', 'skills')    
    search_fields = ['name', 'special', 'skills']

admin.site.register(Career, CareerAdmin)