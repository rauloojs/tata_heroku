from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")

def profile(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
	return HttpResponseRedirect("/reports/user/" + request.user.username)