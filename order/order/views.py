from order import models
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
import datetime

def index(request):
    return render_to_response('index.html', {'sit': 'ok'},
        context_instance=RequestContext(request)) 

def result(request):
    lst = request.POST['listVal'].split(',')
    lst = [int(x) for x in lst]
    ordenator = models.Order(lst)
    lstOrd = ordenator.quicksort()
    media = ordenator.calcMedia()
    return render_to_response('result.html',{'lst': lstOrd, 'media': media},
        context_instance=RequestContext(request))
    
