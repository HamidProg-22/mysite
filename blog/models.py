from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create table Post for blog page and for add a post to blog
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    # image 
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')

    # author
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # title
    title = models.CharField(max_length=255)
    # content
    content = models.TextField()
    # tag

    # category
    category = models.ManyToManyField(Category)
    
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    


    class Meta:
        ordering = ['-created_date']
        # verbose_name = 'پست'
        # verbose_name_plural = 'پست ها'
    # str function for show on ORm database
    def __str__(self):
        # return self.title
        return "{}-{}".format(self.title, self.id)

    def snippets(self):
        # return 'this is snippets'
        return self.content[:100] + '...'

    
    
                                                                
