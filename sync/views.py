from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(" this is the sync service")

# Create your views here.
def detail(request, LogEntry_id):
    return HTTPResponse("The severity is %s." % LogEntry_id)