from django.contrib import admin

from .models import Post, Category   #  or from blog.models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.



# @admin.register(Post) == admin.site.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'   # added item date for easy access
    # empty_value_display = '-emptey-'  # for show empty values of tables
    # fields = ('title', )
    list_display = ('title', 'author', 'counted_views', 'status', 'published_date','created_date')
    list_filter = ('status', 'author' )
    # ordering = ['-created_date']  # - is ordered by dec
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

admin.site.register(Category)

admin.site.register(Post, PostAdmin)