from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def signin(request):
    c = {}
    c.update(csrf(request))
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(username=email, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse(True)
    else:
        raise Http404
