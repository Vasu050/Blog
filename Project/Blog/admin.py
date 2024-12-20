from django.contrib import admin
from.models import Todo
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'date_created')  # Add date_created to list_display
    list_filter = ('author', 'date_created')  # Optional: Add filtering by author or date
    search_fields = ('title', 'description')  # Optional: Add search functionality

    
admin.site.register(Todo,TodoAdmin)