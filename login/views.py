from django.core.context_processors import csrf
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from login.models import RegisteredUsers

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def authorise(request):
    c = {}
    c.update(csrf(request))
    emailID = request.POST.get('email')
    pword = request.POST.get('password')
    user = get_object_or_404(RegisteredUsers, email=emailID)
    pword_from_db = user.get_password()
    if pword == pword_from_db:
        return HttpResponse("Authorisation successful")
    else:
        raise Http404
