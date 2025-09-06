from django.contrib import admin
from .models import Task  # Только модели из текущего приложения


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'due_date', 'created_at']
    list_filter = ['status', 'created_at', 'due_date']
    search_fields = ['title', 'description']
    ordering = ['-created_at']
    readonly_fields = ['created_at']

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'status')
        }),
        ('Дополнительная информация', {
            'fields': ('due_date', 'categories')
        }),
        ('Системная информация', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

