from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'categories']
    search_fields = ['title', 'sub_title']
    
   

admin.site.register(Post, PostAdmin)
