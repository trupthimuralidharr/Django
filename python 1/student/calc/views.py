from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(requests):
    return HttpResponse("Hello guys")

def login(requests):
    return HttpResponse("please login")
