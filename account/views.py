from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Signin successfully.")
            return redirect('dashboard:dashboard')
        else :
            messages.error(request, "Invalid username or password.")
            return redirect('account:signin')
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Signout successfully.")
    return render(request, 'signin.html')
