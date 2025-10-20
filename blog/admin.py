from django.contrib import admin

from .models import Post   #  or from blog.models import Post
# Register your models here.


# @admin.register(Post) == admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'   # added item date for easy access
    # empty_value_display = '-emptey-'  # for show empty values of tables
    # fields = ('title', )
    list_display = ('title', 'counted_views', 'status', 'published_date','created_date')
    list_filter = ('status', )
    ordering = ['-created_date']  # - is ordered by dec
    search_fields = ['title']


   
admin.site.register(Post, PostAdmin)