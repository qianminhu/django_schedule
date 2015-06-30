from django.contrib import admin
from .models import CurrentTask

class TaskAdmin(admin.ModelAdmin):
    search_fields = ['task_type']
    list_filter = ['task_type']
    list_display = ('task_type', 'person_in_charge', 'date_due', 'frequency')

admin.site.register(CurrentTask, TaskAdmin)