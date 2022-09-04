from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(requests):
    first_name = 'Adam Smith'
    age = 20
    return render(requests,'home.html' , {'name':first_name , 'age':age})

def login(requests):
    username = 'Adam12'
    email = '123@fnjs'
    return render(requests, 'login.html', {'username':username , 'email':email})

def signup(requests):
    last_name = 'Smith'
    return render(requests, 'signup.html' , {'lastname': last_name})

def add(requests):
    var1= int(requests.POST['num1'])
    var2= int(requests.POST['num2'])
    var3= var1+var2
    return render(requests, 'add.html' , {'results': var3})