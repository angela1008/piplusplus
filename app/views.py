from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def front(request):
    return render(request, 'front.html')

def profile(request):
    user_id = request.GET.get('id', None)
    userextension = models.UserExtension.objects.get(id=user_id)
    user = User.objects.get(id=user_id)
    return render_to_response('profile_log_in.html',locals())

def group(request):
    return render(request, 'group.html')
