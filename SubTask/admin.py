from django.contrib import admin
from .models import SubTask  # Только модели из текущего приложения


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'task', 'is_completed', 'created_at']
    list_filter = ['is_completed', 'created_at']
    search_fields = ['title', 'description']
    ordering = ['-created_at']
    readonly_fields = ['created_at']

    fieldsets = (
        ('Основная информация', {
            'fields': ('task', 'title', 'description', 'is_completed')
        }),
        ('Системная информация', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


