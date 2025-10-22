# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from blog.models import Post
# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post':post}
    return render(request, 'blog/blog-single.html', context)

# def test(request):
#     posts = Post.objects.all()
#     # posts = Post.objects.filter(status=1)
#     context = {'posts': posts}
#     return render(request, 'blog/test.html', context)  

# def test(request, name):
    
#     context = {'name': name}
#     return render(request, 'blog/test.html', context)

# def test(request, name, family_name, age):
    
#     context = {'name': name, 'family_name': family_name, 'age': age}
#     return render(request, 'blog/test.html', context)

# def test(request, name, family_name, age):
    
#     context = {'name': name, 'family_name': family_name, 'age': age}
#     return render(request, 'blog/test.html', context)

# def test(request, pid):
    
#     context = {'pid':pid}
#     return render(request, 'blog/test.html', context)

# def test(request, pid):
#     post = Post.objects.get(id= pid)
    
#     context = {'post':post}
#     return render(request, 'blog/test.html', context)

# def test(request, pid):
#     post = get_object_or_404(Post, pk=pid)
#     context = {'post':post}
#     return render(request, 'blog/test.html', context)