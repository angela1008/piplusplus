from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from api import models

# Create your views here.
def index(request):
    return render(request, 'index.html')

def profile(request):
    """
    Query user's profile detail.
    TODO judge not exists data
    """
    user_id = request.GET.get('id', None)
    
    ## Profile
    user = User.objects.get(id=user_id)
    userextension = models.UserExtension.objects.get(user=user_id)
    userinterests = models.UserInterest.objects.filter(user=user_id)
    
    ## Group
     # all
    memberships = models.Membership.objects.filter(member=user_id)
    # join
    join_groups = models.Membership.objects.filter(Q(member=user_id) & Q(is_leader=False))
    # leader
    leader_groups = models.Group.objects.filter(leader=user_id)
    return render_to_response('profile_log_in.html',locals())

def group(request):
    return render(request, 'group.html')
