from django.shortcuts import render

# Create your views here.

# this is way not Standard for create a file, after repair 
# from django.http import HttpResponse, JsonResponse
from django.http import HttpResponse

# def http_test(request):
#     # return HttpResponse('Welcome, Hamid')
#     return HttpResponse('<h1>Welcome, Hamid to my project</h1>')

# def json_test(request):
#     return JsonResponse({'name': 'Hamid', 'family': 'Raeisi'})


def index_view(request):
    # return HttpResponse('<h1>Home Page</h1>')
    return render(request, 'website/index.html')

def about_view(request):
    # return HttpResponse('<h1>About Page</h1>')
    return render(request, 'website/about.html')

def contact_view(request):
    # return HttpResponse('<h1>Contact Page</h1>')
    return render(request, 'website/contact.html')
