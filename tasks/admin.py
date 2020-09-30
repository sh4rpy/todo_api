from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'status', 'deadline', )
    list_filter = ('status', 'deadline', )


admin.site.register(Task, TaskAdmin)
