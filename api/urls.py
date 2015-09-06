from django.conf.urls import patterns, include, url

# Function based API views
# from api.views import task_list, task_detail

# Class based API views
from api.views import DoctorList, DoctorDetail, PatientList, PatientDetail, TagList, TagDetail
from . import views

urlpatterns = patterns('',

    # Regular URLs
	# url(r'^doctor/$', doctor_list, name='doctor_list'),
    # url(r'^doctor/(?P<pk>[0-9]+)$', doctor_detail, name='doctor_detail'),

    # Class based URLs,
    url( r'^doctors/$', DoctorList.as_view(), name = 'doctor_list' ),
    url( r'^doctors/(?P<pk>[0-9]+)$', DoctorDetail.as_view(), name = 'doctor_detail' ),
    url( r'^patients/$', PatientList.as_view(), name = 'patient_list' ),
    url( r'^patients/(?P<pk>[0-9]+)$', PatientDetail.as_view(), name = 'patient_detail' ),
    url( r'^tags/$', TagList.as_view(), name = 'tag_list' ),
    url( r'^tags/(?P<pk>[0-9]+)$', TagDetail.as_view(), name = 'tag_detail' ),
    url( r'^search/doctors/$', views.search_doc, name = 'search_doc' ),
    url( r'^search/patients/$', views.search_pat, name = 'search_pat' ),
    url( r'^search/tags/$', views.search_tag, name = 'search_tag' ),
)