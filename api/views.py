from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

from api import models

# Create your views here.
def login(request):
    if request.user.is_authenticated():
        # render to own front page
        return HttpResponseRedirect('/front/?id=%d' %request.user.id)
        
    # If request.user is Anonymous User, we catch informations from request.POST.
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    # And then, use auth.authenticate to authenticate.
    user = auth.authenticate(username=username, password=password)
    
    # Confirm auth.authenticate return user object and not be freeze. 
    if user is not None and user.is_active:
        # Maintain user's login state
        auth.login(request, user)
        return HttpResponseRedirect('/front/')
    else:
        return render_to_response('sign_in.html')
        
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

# TODO not choose classification will error
# TODO after create a new group render to own group page 
# TODO classification(half)
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
    
    if request.method == 'POST':
        leader_id = request.POST.get('leader', None)
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
    
    # return groups
    if request.method == 'GET':
        user_id = request.GET.get('id', None)
        
        # get latest 8 groups
        groups = models.Group.objects.order_by('-created_at')[:8]
        # join
        join_groups = models.Membership.objects.filter(Q(member=user_id) & Q(is_leader=False))
        # leader
        leader_groups = models.Group.objects.filter(leader=user_id)
        return render_to_response('front.html',locals())
    
