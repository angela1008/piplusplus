from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
#from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from api.forms import UserCreateForm as UserCreationForm
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
        if 'next' in request.GET:
            return HttpResponseRedirect('/'+request.GET['next'])
        else:
            return HttpResponseRedirect('/front/?id=%d' %request.user.id)
    else:
        return render_to_response('sign_in.html')
        
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/login/')

    else:
        form = UserCreationForm()
    return render_to_response('sign_up.html', locals())
    
def front(request):
    """
    Get all groups from database.
    """
    # NEED DYNAMIC REQUEST "GET"
    if request.method == 'GET':
        user_id = request.GET.get('id', None)
        
        # return classifications to front.html
        classifications = models.Classification.objects.all()
        
        # get hot 8 groups
        hot_groups = models.Group.objects.order_by('-join_number')[:8]
        # get latest 8 groups
        latest_groups = models.Group.objects.order_by('-created_at')[:8]
        # join
        join_groups = models.Membership.objects.filter(Q(member=user_id))
        # leader
        leader_groups = models.Group.objects.filter(leader=user_id)
        return render_to_response('front.html',locals())
        
    """
    A new user add to a new group.
    """
    is_join = False
    if 'join_group' in request.POST:
        user_id = request.POST.get('member_id', None)
        group_id = request.POST.get('group_id', None)
        user = User.objects.get(id=user_id)
        group = models.Group.objects.get(id=group_id)
        try:
            models.Membership.objects.get(Q(member=user) & Q(group=group))
        except ObjectDoesNotExist:
            models.Membership.objects.create(member=user, group=group, is_leader=False)
            # must use filter instead of get
            models.Group.objects.filter(id=group_id).update(join_number=F('join_number')+1)
            return HttpResponseRedirect('/group/?id=%d' %group.id)
        is_join = True
        # will error
        return render_to_response('front.html',locals())
        
    """
    Add a new group with judging the error when filling the field.
    (not filled in, existing group name)
    """
    # classifications = models.Classification.objects.all()
    
    error = False
    name_error = False
    classification_error = False
    
    if 'add_group' in request.POST:
        leader_id = request.POST.get('leader_id', None)
        leader = User.objects.get(id=leader_id)
        
        name = request.POST.get('name', None)
        if not name :
            name_error = True
            
        classification_id = request.POST.get('classification')
        if not classification_id:
            classification_error = True
        
        # judge whether the group name exists
        if not name_error and not classification_error:
            if models.Group.objects.filter(name=name).exists():
                error = True
            else:
                classification = models.Classification.objects.get(id=classification_id)
                
                create_group = models.Group.objects.create(leader=leader, name=name, classification=classification)
                models.Membership.objects.create(member=leader, group=create_group, is_leader=True)
                group = models.Group.objects.get(id=create_group.id)
                return HttpResponseRedirect('/group/?id=%d' %group.id)
                
        # will error
        return render_to_response('front.html',locals())
    
    
def get_classification_groups(request, classification_id):
    """
    Get groups from different classifications.
    """
    if request.method == 'GET':
        user_id = request.GET.get('id', None)
        
        # return classifications to front.html
        classifications = models.Classification.objects.all()
        classification = models.Classification.objects.get(id=classification_id)
        
        # get groups
        hot_groups = models.Group.objects.filter(classification=classification).order_by('-join_number')[:8]
        latest_groups = models.Group.objects.filter(classification=classification).order_by('-created_at')[:8]
        
        join_groups = models.Membership.objects.filter(Q(member=user_id) & Q(classification=classification))
        
        leader_groups = models.Group.objects.filter(Q(leader=user_id) & Q(classification=classification))
    return render_to_response('front.html',locals())
        
def computer_front(request):
    classification = models.Classification.objects.get(id=1)
    return get_classification_groups(request, classification.id)
    
def build_front(request):
    classification = models.Classification.objects.get(id=2)
    return get_classification_groups(request, classification.id)
    
def math_front(request):
    classification = models.Classification.objects.get(id=3)
    return get_classification_groups(request, classification.id)
    
def healing_front(request):
    classification = models.Classification.objects.get(id=4)
    return get_classification_groups(request, classification.id)

def nature_front(request):
    classification = models.Classification.objects.get(id=5)
    return get_classification_groups(request, classification.id)
    
def art_front(request):
    classification = models.Classification.objects.get(id=6)
    return get_classification_groups(request, classification.id)
    
def society_front(request):
    classification = models.Classification.objects.get(id=7)
    return get_classification_groups(request, classification.id)
    
def manage_front(request):
    classification = models.Classification.objects.get(id=8)
    return get_classification_groups(request, classification.id)
    
def language_front(request):
    classification = models.Classification.objects.get(id=9)
    return get_classification_groups(request, classification.id)

def sport_front(request):
    classification = models.Classification.objects.get(id=10)
    return get_classification_groups(request, classification.id)

def qulification_front(request):
    classification = models.Classification.objects.get(id=11)
    return get_classification_groups(request, classification.id)
    
def test_front(request):
    classification = models.Classification.objects.get(id=12)
    return get_classification_groups(request, classification.id)

def other_front(request):
    classification = models.Classification.objects.get(id=13)
    return get_classification_groups(request, classification.id)
    
def profile(request):
    """
    Query user's profile detail, include judge not exists data.
    """
    user_id = request.GET.get('id', None)
    
    ## Profile
    user = User.objects.get(id=user_id)
    try:
        models.UserExtension.objects.get(user=user_id)
        models.UserInterest.objects.filter(user=user_id)
    except ObjectDoesNotExist:
        userextension = models.UserExtension.objects.create(user=user, gender='', birth=None, location='', self_introduction='')
        userinterests = models.UserInterest.objects.create(user=user, name='')
    
    ## Group
     # all
    memberships = models.Membership.objects.filter(member=user_id)
    # join
    join_groups = models.Membership.objects.filter(Q(member=user_id) & Q(is_leader=False))
    # leader
    leader_groups = models.Group.objects.filter(leader=user_id)
    return render_to_response('profile_log_in.html',locals())
    
def group(request):
    group_id = request.GET.get('id',None)
    if group_id:
        user_in_group = False
        if request.user.is_authenticated():
            group = models.Group.objects.get(id=group_id)
            memberships = models.Membership.objects.filter(group=group)
            for membership in memberships:
                if membership.member == request.user:
                    user_in_group = True
                    break
        return render(request, 'group.html',locals())