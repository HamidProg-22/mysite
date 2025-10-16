from django.shortcuts import render

# Create your views here.

# this is way not Standard for create a file, after repair 
from django.http import HttpResponse, JsonResponse

def http_test(request):
    # return HttpResponse('Welcome, Hamid')
    return HttpResponse('<h1>Welcome, Hamid to my project</h1>')

def json_test(request):
    return JsonResponse({
        'name': 'Hamid',
        'family': 'Raeisi'
    })

