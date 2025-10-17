

from django.urls import path
# the follow codes is generate by me
# from website.views import http_test # or from .views import http_test
# from website.views import json_test
from website.views import *

app_name = 'website'

urlpatterns = [
    # path('http-test', http_test),
    # path('json-test', json_test),
    path('', index_view, name= 'index'),
    path('about', about_view, name= 'about'),
    path('contact', contact_view, name= 'contact')
]