from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader

from userapp.models import TwitterUser

# Create your views here.
def index(request):
	request.session['user_name'] = '@janakact'
	#HttpResponseRedirect(reverse('userapp:index'))
	return home(request)

def home(request):
	user = TwitterUser.objects.get(user_name=request.session['user_name'])
	user.setup()
	tweets = user.getTweets()
	profile = user.getProfile()
	template = loader.get_template('userapp/home.html')
	context = RequestContext(request, {'tweets': tweets,'profile':profile})
	return HttpResponse(template.render(context))
	

def login(request):
	return HttpResponse("Please Login")