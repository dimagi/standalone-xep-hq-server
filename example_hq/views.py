from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import XForm

def index(request, template="HQ.html"):
    xform_id = request.GET.get('xform_id', '')
    xform = XForm.get(xform_id)
    c = {
        'xform': xform,
    }
    c.update(csrf(request))
    
    return render_to_response(template, c)