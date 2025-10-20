from django.contrib import admin

from .models import Post   #  or from blog.models import Post
# Register your models here.

admin.site.register(Post)