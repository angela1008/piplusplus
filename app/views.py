from django.shortcuts import render
from django.shortcuts import render_to_response

from api import models

# Create your views here.
def index(request):
    return render_to_response('index.html', locals())

