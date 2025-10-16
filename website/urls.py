

from django.urls import path
# the follow codes is generate by me
from website.views import http_test # or from .views import http_test
from website.views import json_test

urlpatterns = [
    path('http-test', http_test),
    path('json-test', json_test)
]