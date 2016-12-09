from django.conf.urls import url

from .views import (
	job_list,
	job_create,
	job_detail,
	job_edit,
	job_delete
)

urlpatterns = [
    url(r'^$', job_list, name='index'),
    url(r'^create/$', job_create, name='create'),
    url(r'^(?P<pk>[0-9]+)/$', job_detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', job_edit, name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', job_delete, name='delete'),
]