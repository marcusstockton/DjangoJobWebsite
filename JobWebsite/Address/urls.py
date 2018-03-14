from django.urls import path

from .views import (
	address_list,
	address_create,
	address_detail,
	address_edit,
	address_delete
)
app_name="addresses"
urlpatterns = [
    path('', address_list, name='index'),
    path('create/', address_create, name='create'),
    path('<uuid:pk>/', address_detail, name='detail'),
    path('<uuid:pk>/edit/', address_edit, name='edit'),
    path('<uuid:pk>/delete/', address_delete, name='delete'),
]