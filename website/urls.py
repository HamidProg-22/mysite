

from django.urls import path
# the follow codes is generate by me
# from website.views import http_test # or from .views import http_test
# from website.views import json_test
from website.views import *

urlpatterns = [
    # path('http-test', http_test),
    # path('json-test', json_test),
    path('', index_view),
    path('about', about_view),
    path('contact', contact_view)
]