from django.shortcuts import render
from djang.contrib.auth import authenticate, login

# Create your views here.

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            #Redirect to a success page
        else:
            print('Disabled account')
            #Return a 'disabled account' error message

    else:
        print('Invalid login')
        #Return an 'invalid login' error message

def logout_view(request):
    logout(request)
    #Redirect to a success page
