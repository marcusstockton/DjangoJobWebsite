from django.urls import path

from .views import (
	company_list,
	company_create,
	company_detail,
	company_edit,
	company_delete
)

app_name="company"
urlpatterns = [
    path('', company_list, name='index'),
    path('create/', company_create, name='create'),
    path('<uuid:pk>/', company_detail, name='detail'),
    path('<uuid:pk>/edit/', company_edit, name='edit'),
    path('<uuid:pk>/delete/', company_delete, name='delete'),
]