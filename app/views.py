from django.shortcuts import render
from django.contrib import auth
# from datetime import datetime

# Create your views here.
def sign_in(request):
    return render(request, 'sign_in.html')
    
def sign_up(request):
    return render(request, 'sign_up.html')

def index(request):
    return render(request, 'index.html')

def front(request):
    return render(request, 'front.html')

def profile(request):
    return render(request, 'profile.html')

def group(request):
    return render(request, 'group.html')
