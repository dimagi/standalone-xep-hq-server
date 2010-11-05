from couchdbkit.ext.django.schema import *
from django.http import HttpResponseForbidden

class XForm(Document):
    form = StringProperty()
    @property
    def id(self):
        return self._id
        
def get_xform(xform_id):
    return XForm.get(xform_id).form
    
def put_xform(xform_id, form):
    xform = XForm.get(xform_id)
    xform.form = form
    xform.save()

def authorize_xform_edit(view):
    def authorized_view(request, xform_id):
        authorized = True
        # Do some sort of authorization
        if authorized:
            return view(request, xform_id)
        else:
            return HttpResponseForbidden()
    return authorized_view