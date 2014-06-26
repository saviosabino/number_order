from order.core import models
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie
import datetime

@ensure_csrf_cookie
def index(request):
    return render_to_response('index.html', {},
        context_instance=RequestContext(request)) 

def result(request):
    lst = request.POST['listVal'].split(',')
    lst = [int(x) for x in lst]
    ordenator = models.Order(lst)
    lstOrdered = ordenator.quicksort()
    media = ordenator.calcMedia()
    return render_to_response('result.html',{'lst': lstOrdered, 'media': media},
        context_instance=RequestContext(request))
    
