from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'stock_name', 'created_at')
    search_fields = ('title', 'stock_name')
