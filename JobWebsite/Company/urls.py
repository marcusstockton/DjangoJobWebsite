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
    path('<int:pk>/', company_detail, name='detail'),
    path('<int:pk>/edit/', company_edit, name='edit'),
    path('<int:pk>/delete/', company_delete, name='delete'),
]