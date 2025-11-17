from django.contrib import admin

from .models import Post, Category, Comment  #  or from blog.models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.



# @admin.register(Post) == admin.site.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'   # added item date for easy access
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views', 'status', 'published_date','created_date')
    list_filter = ('status', 'author' )
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'  
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approved','created_date')
    list_filter = ('post', 'approved' )
    search_fields = ['name', 'post']
    

admin.site.register(Comment,CommentAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)