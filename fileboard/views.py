from django.core.context_processors import csrf
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from login.models import RegisteredUsers
from fileboard.models import File

# Create your views here.

def index(request):
    return render(request, 'fileboard/index.html')

