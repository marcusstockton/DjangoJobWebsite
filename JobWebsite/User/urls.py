from django.urls import path

from .views import (
	user_list,
	user_create,
	user_detail,
	user_edit,
	user_delete,
)

app_name = 'users'
urlpatterns = [
	path('', user_list, name='index'),
	path('<uuid:pk>/', user_detail, name='detail'),
	path('<uuid:pk>/edit/', user_edit, name='edit'),
	path('<uuid:pk>/delete/', user_delete, name='delete'),
	path('create/', user_create, name='create'),
]
