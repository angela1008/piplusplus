from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from api import models

# Create your views here.
def index(request):
    return render(request, 'index.html')

# TODO not choose classification will error
# TODO after create a new group render to own group page 
def front(request):
    """
    Add a new group with judging the error when filling the field.
    (not filled in, existing group name)
    """
    classifications = models.Classification.objects.all()
    
    error = False
    leader_error = False
    name_error = False
    classification_error = False
    group = None
    
    if 'ok' in request.POST:
        leader_id = request.POST.get('leader')
        leader = User.objects.get(id=leader_id)
        
        name = request.POST.get('name')
        # judge whether the group name exists
        try:
            models.Group.objects.get(name=name)
        except ObjectDoesNotExist:
            classification_id = request.POST.get('classification')
            classification = models.Classification.objects.get(id=classification_id)
            
            # judge whether the field is filled in
            if not name :
                name_error = True
            if not classification:
                classification_error = True
            if not leader_error and not name_error and not classification_error:
                create_group = models.Group.objects.create(leader=leader, name=name, classification=classification)
                models.Membership.objects.create(member=leader, group=create_group, is_leader=True)
                group = models.Group.objects.get(id=create_group.id)
            # if normal using then return directly,not got to error=True
            return render_to_response('front.html',locals())
            
        # if "ObjectDoesExist" then set error and return to front page
        error = True
        
    return render_to_response('front.html',locals())
    
     
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
