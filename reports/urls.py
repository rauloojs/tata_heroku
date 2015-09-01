from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'), 
	url(r'^send/$', views.send, name='send'),
	url(r'^(?P<rep_id>[0-9]+)/results/(?P<status>[0-9]+)/$', views.results, name='results'),
]