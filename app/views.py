from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from api import models

# Create your views here.
def index(request):
    return render(request, 'index.html')

def group(request):
    return render(request, 'group.html')
