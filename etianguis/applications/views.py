#from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    template = loader.get_template('applications/index.html')
    return HttpResponse(template.render(context))
