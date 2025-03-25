from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    return render(request, 'profile.html')
