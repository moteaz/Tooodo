from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'owner', 'created_at', 'due_date')
    list_filter = ('status', 'created_at', 'due_date')
    search_fields = ('title', 'description', 'owner__username')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)