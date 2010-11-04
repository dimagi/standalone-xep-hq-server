from couchdbkit.ext.django.schema import *

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
    