from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.http import HttpResponse

# Create your views here.
def my_view(request):
   # Translators: This message appears on the my_view only
    output = _("Welcome to my site à moi.")
    return HttpResponse(output)