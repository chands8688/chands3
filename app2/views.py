from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def chandu(request):
    return HTTPResponse('This is from chandu')
    