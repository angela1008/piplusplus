from django.shortcuts import render

from api import models

# Create your views here.
def index(request):
    return render(request, 'index.html')

