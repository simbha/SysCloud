from django.core.context_processors import csrf
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from login.models import RegisteredUsers, Session
from fileboard.models import UserAccessToken
from dropbox import client, session, rest

# Create your views here.

def getAccessToken(request, sess):
    request_token = sess.obtain_request_token()
    url = sess.build_authorize_url(request_token)
    return render(request, 'fileboard/authorise.html', {'url': url})

def getUserFileboard(request, user):
    APP_KEY = 'zcw39nd2i33p78c'
    APP_SECRET = 'qnuut37muivao2v'
    ACCESS_TYPE = 'dropbox'
    
    sess = session.DropboxSession(APP_KEY,APP_SECRET,ACCESS_TYPE)
    try:
        user_access_token = UserAccessToken.objects.get(user=user)
        return render(request, 'fileboard/index.html')
    except UserAccessToken.DoesNotExist:
        return getAccessToken(request, sess)
    
def permission(request):
    return True

def index(request, email_id, session_key):
    user = get_object_or_404(RegisteredUsers, email=email_id)
    session_objects = Session.objects.filter(user=user)
    session_exists = False
    for session_object in session_objects:
        session_key_from_db = session_object.get_session_key()
        if session_key == session_key_from_db:
            session_exists = True
    if session_exists:
        return getUserFileboard(request, user)
    else:
        raise Http404

