from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse,request,HttpResponseRedirect
from django.contrib import messages
from mysite import models
from mysite import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
# Create your views here.

def index(request):
    polls = models.Poll.objects.all()
    messages.add_message(request,messages.INFO,'欢迎')
    template = get_template('index.html')
    html = template.render(context=locals(),request = request)
    return HttpResponse(html)

def poll(request,pollid):
    try:
        poll=  models.Poll.objects.get(id = pollid)
    except:
        poll = None
    if poll is not None:
        pollitems = models.PollItem.objects.filter(poll = poll).order_by('-vote')
    template = get_template('poll.html')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def vote(request,pollid,pollitemid):
    try:
        pollitem = models.PollItem.objects.get(id = pollitemid)
    except:
        pollitem = None
    if pollitem is not None:
        pollitem.vote = pollitem.vote + 1
        pollitem.save()
    target_url = '/poll/' + pollid
    return HttpResponseRedirect(target_url)

def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username=login_name,password = login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request,user)
                    messages.add_message(request,messages.SUCCESS,'成功登陆')
                    return HttpResponseRedirect('/')
                else:
                    messages.add_message(request,messages.WARNING,'账号尚未启用')
            else:
                messages.add_message(request, messages.WARNING, '登录失败')
        else:
            messages.add_message(request,messages.INFO,'请检查输入的字段内容')
    else:
        login_form = forms.LoginForm()
    template = get_template('login.html')
    html = template.render(context=locals(),request = request)
    return HttpResponse(html)

def logout(request):
    auth.logout(request)
    messages.add_message(request,messages.INFO,'成功注销')
    return HttpResponseRedirect('/')