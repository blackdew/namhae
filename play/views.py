from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from . import models

def hello(req):
    return HttpResponse("hello")

def mission(req, key):
    obj = get_object_or_404(models.Mission, key=key)
    return render(req, 'mission.html', {'html': obj.html()})