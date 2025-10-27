from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag
def hello():
    return 'Hello'

# @register.simple_tag()
# def function(a):
#     return a + 2

@register.simple_tag(name='plustwo')    # add a name for function
def function(a=6):      # defin default value for arghoman a = 6
    return a + 2

@register.simple_tag(name='totalpost')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value, arg=20):
    return value[:arg] + '...'

@register.inclusion_tag('popularposts.html')
def popularposts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:2]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts}