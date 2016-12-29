from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def front(request):
    return render(request, 'front.html')

def profile(request):
    return render(request, 'profile.html')

def group(request):
    return render(request, 'group.html')
