from django.shortcuts import render , redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User , auth

# Create your views here.
def accounts(requests):
    return render(requests, 'accounts.html')

def login(requests):
    if requests.method == 'POST':
        username=requests.POST['username']
        password=requests.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(requests,user)
            print('login sucessful')
            return redirect('/')
    else:
        return render(requests, 'login.html')

def signup(requests):
    if requests.method == 'POST':
        firstName = requests.POST['first_name']
        lastName = requests.POST['last_name'] 
        email = requests.POST['email'] 
        username = requests.POST['username'] 
        password = requests.POST['password']  
        password2 = requests.POST['password2'] 

        if password == password2:

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                password2=password2,
                first_name = firstName,
                last_name = lastName
            )
            return redirect('/')
        else: 
            print('wrong password')
    else:
        return render(requests, 'signup.html')
