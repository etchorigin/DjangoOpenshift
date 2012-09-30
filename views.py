import os
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login



def home(request):
    return render_to_response('home/home.html')

def accounthome(request):
    if request.user.is_authenticated():
        return render_to_response('home/profile.html')
    else:
        return render_to_response('home/accounthome.html')
	
@login_required	
def profile(request):
    return render_to_response('home/profile.html')
