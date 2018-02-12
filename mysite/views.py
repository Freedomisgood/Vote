from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse,request,HttpResponseRedirect
from django.contrib import messages
from mysite import models
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