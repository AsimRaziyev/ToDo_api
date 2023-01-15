from django.contrib import admin

# Register your models here.

from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'deadline', 'performed']
    fields = ['title', 'description', 'deadline', 'performed']


admin.site.register(Task, TaskAdmin)
