from django.conf.urls import url

from .views import (
	user_list,
	user_create,
	user_detail,
	user_edit,
	user_delete
)
urlpatterns = [
	url(r'^$', user_list, name='index'),
	url(r'^(?P<pk>[0-9]+)/$', user_detail, name='detail'),
	url(r'^(?P<pk>[0-9]+)/edit/$', user_edit, name='edit'),
	url(r'^(?P<pk>[0-9]+)/delete/$', user_delete, name='delete'),
	url(r'^create/$', user_create, name='create'),
]
