from django.urls import path

from . import views

app_name = "attachments"
urlpatterns = [
    path('', views.attachment_list, name='index'),
    path('<uuid:pk>/', views.DetailView, name='detail'),
    path('<uuid:pk>/edit/', views.EditView, name='edit'),
    path('<uuid:pk>/delete/', views.DeleteView, name='delete'),
]
