from django.db import models

# Create your models here.

# Create table Post for blog page and for add a post to blog
class Post(models.Model):
    # image 
    # author
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    # category
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

    
    
                                                                
