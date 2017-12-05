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
    path('<int:pk>/', address_detail, name='detail'),
    path('<int:pk>/edit/', address_edit, name='edit'),
    path('<int:pk>/delete/', address_delete, name='delete'),
]