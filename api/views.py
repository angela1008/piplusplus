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
from django.core.urlresolvers import reverse_lazy
# from django.views.generic.edit import UpdateView
from django.views.generic import UpdateView
from base64 import b64decode
from django.core.files.base import ContentFile
from django.core.files import File
#from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from api.forms import UserCreateForm as UserCreationForm
from api import forms
from api import models
import os

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
    return HttpResponseRedirect('http://piplusplus-u10216026.c9users.io/')
    
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
        if user_id:
            user = User.objects.get(id=user_id)
        
            # join
            join_groups = models.Membership.objects.filter(Q(member=user_id))
            # leader
            leader_groups = models.Group.objects.filter(leader=user_id)
        # return classifications to front.html
        classifications = models.Classification.objects.all()
        classfication1 = models.Classification.objects.get(id=1)
        
        # get hot 8 groups
        hot_groups = models.Group.objects.order_by('-join_number')[:8]
        # get latest 8 groups
        latest_groups = models.Group.objects.order_by('-created_at')[:8]
            
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
            models.Membership.objects.create(member=user, group=group, classification=group.classification,is_leader=False)
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
                models.Membership.objects.create(member=leader, group=create_group, classification=classification,is_leader=True)
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
        user = User.objects.get(id=user_id)
        
        # return classifications to front.html
        classifications = models.Classification.objects.all()
        classification = models.Classification.objects.get(id=classification_id)
        
        # get groups
        hot_groups = models.Group.objects.filter(classification=classification).order_by('-join_number')[:8]
        latest_groups = models.Group.objects.filter(classification=classification).order_by('-created_at')[:8]
        
        join_groups = models.Membership.objects.filter(Q(member=user) & Q(classification=classification))
        
        leader_groups = models.Group.objects.filter(Q(leader=user) & Q(classification=classification))
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
    
def profile(request, user):
    """
    Query user's profile detail, include judge not exists data.
    """
    if request.method=='GET':
        user = User.objects.get(username=user)
        
        is_owner = False
        if user==request.user:
            is_owner=True
            
        try:
            userextention = models.UserExtension.objects.get(user=user)
            userinterests = models.UserInterest.objects.filter(user=user)
        except ObjectDoesNotExist:
            models.UserExtension.objects.create(user=user, name='', gender='', birth=None, location='', self_introduction='')
            models.UserInterest.objects.create(user=user, name='')
        
        ## Group
        #  # all
        memberships = models.Membership.objects.filter(member=user)
        # # join
        join_groups = models.Membership.objects.filter(Q(member=user) & Q(is_leader=False))
        # # leader
        leader_groups = models.Group.objects.filter(leader=user)
        return render_to_response('profile_owner.html',locals())
        
    """
    Update user's detail.(Edit)
    """
    if request.method=='POST':
        username = user
        user = User.objects.get(username=user)
        userextension = models.UserExtension.objects.get(user=user)
        userinterest = models.UserInterest.objects.get(user=user)
            
        if 'edit_name' in request.POST:
            user_name = request.POST['name']
            user.first_name = user_name
            user.save()
        if 'edit_profile' in request.POST:
            if 'gender' in request.POST:
                user_gender = request.POST['gender']
                userextension.gender = user_gender
            user_birth = request.POST['birth']
            user_location = request.POST['location']
            user_email = request.POST['email']
            try:
                token = user_birth.split("/")
                user_birth = "%s-%s-%s"%(token[2],token[0],token[1])
                userextension.birth = user_birth
            except:
                pass
            userextension.location = user_location
            user.email = user_email
            userextension.save()
            user.save()
        elif 'edit_introduction' in request.POST:
            user_introduction = request.POST['introduction']
            if 'interest' in request.POST:
                user_interests = request.POST['interest']
                userinterest.self_introduction = user_interests
            userextension.self_introduction = user_introduction
            userextension.save()
            userinterest.save()
            
        elif 'update_profile_pic' in request.POST:
            up_file_b64 = request.POST['image']
            print up_file_b64
            destination = open('/tmp/' + username , 'wb+')
            destination.write(b64decode(up_file_b64.split(",")[1]))
            destination.close()
            if os.path.exists('static/media/user/%s'%(username)):
                os.remove('static/media/user/%s'%(username))
            userextension.user_pic.save('/user/%s'%(username), File(open('/tmp/' + username, 'r')))
            userextension.save()
        return HttpResponseRedirect('/profile/%s' %request.user)


def group(request):
    group_id = request.GET.get('id',None)
    if request.method=='POST':
        group = models.Group.objects.get(id=group_id)
        if 'join_group' in request.POST:
            is_join=False
            user = request.user
            try:
                models.Membership.objects.get(Q(member=user) & Q(group=group))
            except ObjectDoesNotExist:
                models.Membership.objects.create(member=user, group=group, classification=group.classification, is_leader=False)
                # must use filter instead of get
                models.Group.objects.filter(id=group_id).update(join_number=F('join_number')+1)
                return HttpResponseRedirect('/group/?id=%s' %group_id)
            is_join = True
            return render_to_response('group.html',locals())
        try:
            member = models.Membership.objects.get(member=request.user, group=group)
        except:
            return HttpResponseRedirect('/group/?id=%s' %group_id)
        if 'add_article' in request.POST:
            title = request.POST['name']
            content = request.POST['content']
            discussion = models.Discussion.objects.create(creater=member, group=group, title=title, content=content)
        elif 'add_comment' in request.POST:
            discussion_id = request.POST['discussion_id']
            discussion = models.Discussion.objects.get(id=discussion_id)
            discussion.comment_number += 1
            discussion.save()
            content = request.POST['comment']
            comment = models.Comment.objects.create(creater=member, content=content, discussion=discussion)
        elif 'discussion_heart' in request.POST:
            discussion_id = request.POST['discussion_id']
            discussion = models.Discussion.objects.get(id=discussion_id)
            try:
                discussion_heart = models.DiscussionHeart.objects.get(member=member, discussion=discussion, group=group)
                if discussion_heart.is_heart:
                    discussion.heart_number -= 1
                    discussion.save()
                    discussion_heart.is_heart = False
                    discussion_heart.save()
                else:
                    discussion.heart_number += 1
                    discussion.save()
                    discussion_heart.is_heart = True
                    discussion_heart.save()
            except ObjectDoesNotExist:
                discussion_heart = models.DiscussionHeart.objects.create(member=member, discussion=discussion, group=group, is_heart=True)
                discussion.heart_number += 1
                discussion.save()
        elif 'comment_heart' in request.POST:
            discussion_id = request.POST['discussion_id']
            comment_id = request.POST['comment_id']
            discussion = models.Discussion.objects.get(id=discussion_id)
            comment = models.Comment.objects.get(id=comment_id)
            try:
                comment_heart = models.CommentHeart.objects.get(member=member, comment=comment, discussion=discussion)
                if comment_heart.is_heart:
                    comment.heart_number -= 1
                    comment.save()
                    comment_heart.is_heart = False
                    comment_heart.save()
                else:
                    comment.heart_number += 1
                    comment.save()
                    comment_heart.is_heart = True
                    comment_heart.save()
            except ObjectDoesNotExist:
                comment_heart = models.CommentHeart.objects.create(member=member, comment=comment, discussion=discussion, is_heart=True)
                comment.heart_number += 1
                comment.save()
        elif 'add_event' in request.POST:
            event_name = request.POST['event_name']
            content = request.POST['content']
            event_start_date = request.POST['event_start_date']
            event_start_time = request.POST['event_start_time']
            event_end_date = request.POST['event_end_date']
            event_end_time = request.POST['event_end_time']
            token = event_start_date.split("/")
            event_start_date = "%s-%s-%s"%(token[2],token[0],token[1])
            token = event_end_date.split("/")
            event_end_date = "%s-%s-%s"%(token[2],token[0],token[1])
            event_start_time = datetime.strptime(event_start_time, "%I:%M %p").strftime("%H:%M")
            event_end_time = datetime.strptime(event_end_time, "%I:%M %p").strftime("%H:%M")
            location = request.POST['location']
            event = models.Event.objects.create(creater=member, title=event_name, content=content, group=group, start_date=event_start_date, start_time=event_start_time, end_date=event_end_date, end_time=event_end_time, location=location)
        elif 'event_join' in request.POST:
            event_id = request.POST['event_id']
            event_join = int(request.POST['event_join'])
            event = models.Event.objects.get(id=event_id)
            try:
                eventship = models.EventShip.objects.get(member=member, event=event, group=group)
                print event_join
                if eventship.is_join == event_join:
                    print eventship.is_join,event_join
                elif event_join == 1:
                    event.join_number += 1
                    event.save()
                    eventship.is_join = 1
                    eventship.save()
                elif eventship.is_join == 1:
                    event.join_number -= 1
                    event.save()
                    eventship.is_join = event_join
                    eventship.save()
                else:
                    eventship.is_join = event_join
                    eventship.save()
            except ObjectDoesNotExist:
                eventship = models.EventShip.objects.create(member=member, event=event, group=group, is_join=event_join)
                if event_join ==1:
                    event.join_number += 1
                    event.save()
        elif 'add_task' in request.POST:
            title = request.POST['title']
            content = request.POST['content']
            task_end_date = request.POST['task_end_date']
            task_end_time = request.POST['task_end_time']
            token = task_end_date.split("/")
            task_end_date = "%s-%s-%s"%(token[2],token[0],token[1])
            task_end_time = datetime.strptime(task_end_time, "%I:%M %p").strftime("%H:%M")
            task = models.Task.objects.create(title=title, content=content, group=group, deadline_date=task_end_date, deadline_time=task_end_time)
        elif 'task_finished' in request.POST:
            task_id = request.POST['task_id']
            task = models.Task.objects.get(id=task_id)
            try:
                task_finished = models.TaskShip.objects.get(member=member, task=task, group=group)
                if task_finished.is_finished:
                    task.finished_number -= 1
                    task.save()
                    task_finished.is_finished = False
                    task_finished.save()
                else:
                    task.finished_number += 1
                    task.save()
                    task_finished.is_finished = True
                    task_finished.save()
            except ObjectDoesNotExist:
                task_finished = models.TaskShip.objects.create(member=member, task=task, group=group, is_finished=True)
                task.finished_number += 1
                task.save()
        elif 'edit_group' in request.POST:
            group_name = request.POST['name']
            group_introduction = request.POST['description']
            if member.is_leader:
                group.name = group_name
                group.group_introduction = group_introduction
                group.save()
        elif 'update_group_pic' in request.POST:
            if member.is_leader:
                #up_file = request.FILES['image']
                up_file_b64 = request.POST['image'] #
                #image_data = b64decode(up_file_b64) #
                #print up_file_b64
                destination = open('/tmp/' + (group_id) , 'wb+')
                destination.write(b64decode(up_file_b64.split(",")[1]))
                destination.close()

                #destination.write(ContentFile(image_data, (group_id)+'.png')) #
                #for chunk in up_file.chunks():
                #    destination.write(chunk)
                #destination.close()

                
                if os.path.exists('static/media/group/%s'%(group_id)):
                    os.remove('static/media/group/%s'%(group_id))
                #group.group_pic.save('/group/%s'%(group_id), File(open('/tmp/' + up_file.name, 'r')))
                group.group_pic.save('/group/%s'%(group_id), File(open('/tmp/' + (group_id), 'r')))
                group.save()
        return HttpResponseRedirect('/group/?id=%s'%group_id)
    else:
        if group_id:
            user_in_group = False
            group = models.Group.objects.get(id=group_id)
            #group.group_pic = 'static/media/group/default.png'
            #group.save()
            memberships = models.Membership.objects.filter(group=group)
            for membership in memberships:
                if membership.member == request.user:
                    user_in_group = True
                    break
            discussions = models.Discussion.objects.filter(group = group)
            comments = models.Comment.objects.filter(discussion__in = discussions)
            events = models.Event.objects.filter(group = group)
            tasks = models.Task.objects.filter(group = group)
            if request.user.is_authenticated():
                if user_in_group:
                    member = models.Membership.objects.get(member=request.user, group=group)
                    eventships = models.EventShip.objects.filter(member=member,group=group)
                    for event in events:
                        in_event = False
                        for eventship in eventships:
                            if eventship.event ==event:
                                event.is_join = eventship.is_join
                                in_event = True
                        if not in_event:
                            event.is_join=0
                    taskships = models.TaskShip.objects.filter(member=member,group=group)
                    for task in tasks:
                        in_task = False
                        for taskship in taskships:
                            if taskship.task == task:
                                task.is_finished=taskship.is_finished
                                in_task = True
                        if not in_task:
                            task.is_finished=False

            return render(request, 'group.html',locals())