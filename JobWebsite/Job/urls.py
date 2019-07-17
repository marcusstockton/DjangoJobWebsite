from django.urls import path

from .views import (
    job_list,
    job_create,
    job_detail,
    job_edit,
    job_delete,
    job_apply,
    job_import,
    job_applications
)
app_name = 'jobs'
urlpatterns = [
    path('', job_list, name='index'),
    path('create/', job_create, name='create'),
    path('<uuid:pk>/', job_detail, name='detail'),
    path('<uuid:pk>/edit/', job_edit, name='edit'),
    path('<uuid:pk>/delete/', job_delete, name='delete'),
    path('<uuid:pk>/apply/', job_apply, name='apply'),
    path('<uuid:pk>/applications/', job_applications, name='applications'),
    path('import/', job_import, name='import')
]
