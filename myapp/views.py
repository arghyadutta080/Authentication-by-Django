from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def index(request) :
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return render(request, 'index.html')
    else:
        # Do something for anonymous users.
        return redirect ('login')
    


def loginUser(request):
    if request.method == 'POST' :
        username = request.POST.get('loginname')
        password = request.POST.get('loginpassword')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('index')
        else:
            # No backend authenticated the credentials
            return redirect('login')   

    return render(request, 'login.html')



def signup(request):
    if request.method == 'POST' :
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        return redirect('index')
    
    return render(request, 'signup.html')        



def logoutPage(request):
    logout(request)
    return redirect('login')    