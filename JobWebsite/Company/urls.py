from django.conf.urls import url

from .views import (
	company_list,
	company_create,
	company_detail,
	company_edit,
	company_delete
)

urlpatterns = [
    url(r'^$', company_list, name='index'),
    url(r'^create/$', company_create, name='create'),
    url(r'^(?P<pk>[0-9]+)/$', company_detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', company_edit, name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', company_delete, name='delete'),
]