from django.contrib import admin
from .models import Blogger, Blog, Comment

# Register your models here.

# admin.site.register(Blogger)
# admin.site.register(Blog)
# admin.site.register(Comment)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'content')

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blogger', 'create_date')

class BlogInline(admin.TabularInline):
    model = Blog
    extra = 0

@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro')
    inlines = [BlogInline]