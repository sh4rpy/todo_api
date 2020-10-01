from django.contrib import admin

from .models import Task, TaskHistory


class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'status', 'deadline', )
    list_filter = ('status', 'deadline', )
    search_fields = ('title', )


class TaskHistoryAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'title', 'status', 'deadline', )


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskHistory, TaskHistoryAdmin)
