from django.contrib import admin
from django.db import models
#from tinymce.widgets import TinyMCE
from app.blog.models import Post, Category, SubscribeUsers



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'user', 'category']
	list_filter = ['publish', 'created']
	prepopulated = {'slug': ('title', )}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_filter = ['name']

admin.site.register(SubscribeUsers)
