from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import XForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request, template="HQ.html"):
    xform_id = request.GET.get('xform_id', '')
    if not xform_id:
        xform = XForm(form="<xform>This is a new xform</xform>")
        xform.save()
        return HttpResponseRedirect(reverse('example_hq.views.index') + '?xform_id=%s' % xform._id)
    xform = XForm.get(xform_id)
    c = {
        'xform': xform,
    }
    c.update(csrf(request))
    
    return render_to_response(template, c)