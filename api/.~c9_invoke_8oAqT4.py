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

from api.forms import UserCreateForm as UserCreationForm
from api import models

# Create your views here.
def login(request):
    if request.user.is_authenticated():
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
    
## TODO not choose classification will error
def front(request):
    """
    Get groups from database.
    """
    # NEED DYNAMIC REQUEST "GET"
    if request.method == 'GET':
        user_id = request.GET.get('id', None)
        
        # return classifications to front.html
        classifications = models.Classification.objects.all()
        
        # get latest 8 groups
        groups = models.Group.objects.order_by('-created_at')[:8]
        # join
        join_groups = models.Membership.objects.filter(Q(member=user_id) & Q(is_leader=False))
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
    if request.method == 'POST':
        if 'name' in request.POST and 'article_id' in request.POST:
            article_id=request.POST.get('article_id', None)
            name = request.POST.get('name')
            
            
    else:
        
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


























        return render(request, 'group.html',locals())