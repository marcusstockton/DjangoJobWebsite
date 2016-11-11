from django.conf.urls import url
from django.contrib import admin

from .views import (
	address_list,
	address_create,
	address_detail,
	address_edit,
	address_delete
)

urlpatterns = [
    url(r'^$', address_list, name='index'),
    url(r'^create/$', address_create),
    url(r'^(?P<pk>[0-9]+)/$', address_detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', address_edit, name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', address_delete, name='delete'),
]