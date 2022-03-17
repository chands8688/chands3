from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def app1_fun(request):
    return HTTPResponse('this rom  app1')