from django.urls import path

from . import views

app_name="attachments"
urlpatterns = [
    path('', views.attachment_list, name='index'),
    path('<int:pk>/', views.DetailView, name='detail'),
    path('<int:pk>/edit/', views.EditView, name='edit'),
    path('<int:pk>/delete/', views.DeleteView, name='delete'),
]
