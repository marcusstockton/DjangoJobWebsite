from django.urls import path

from .views import (
	job_list,
	job_create,
	job_detail,
	job_edit,
	job_delete
)
app_name = 'jobs'
urlpatterns = [
    # path(r'^$', job_list, name='index'),
    # path(r'^create/$', job_create, name='create'),
    # path(r'^(?P<pk>[0-9]+)/$', job_detail, name='detail'),
    # path(r'^(?P<pk>[0-9]+)/edit/$', job_edit, name='edit'),
    # path(r'^(?P<pk>[0-9]+)/delete/$', job_delete, name='delete'),
    path('', job_list, name='index'),
    path('create/', job_create, name='create'),
    path('<int:pk>/', job_detail, name='detail'),
    path('<int:pk>/edit/', job_edit, name='edit'),
    path('<int:pk>/delete/', job_delete, name='delete'),
]