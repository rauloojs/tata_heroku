from django.shortcuts import render_to_response
from django.template import RequestContext
 
def index(request):
	logged = False
	if request.user is not None and request.user.is_active:
		logged = True
	return render_to_response('home/index.html', {'logged': logged, 'user': request.user})