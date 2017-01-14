from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
#from django.contrib.auth.forms import UserCreationForm

from api.forms import UserCreateForm as UserCreationForm
from api import models

# Create your views here.
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/front/')
        
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
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/login/')

    else:
        form = UserCreationForm()
    return render_to_response('sign_up.html',locals())
    
def front_group(request):
    """
    classification with all/member/your group,
    all group include hot/latest
    """
    if request.method == 'GET':
        groups = models.Group.objects.all()
        request.session['groups'] = groups
        return render_to_response('front.html',locals())

# TODO not choose classification will error
# TODO after create a new group render to own group page 
def front_add(request):
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
            
    if request.method == 'GET':
        error = True
        
    return render_to_response('front.html',locals())
    
