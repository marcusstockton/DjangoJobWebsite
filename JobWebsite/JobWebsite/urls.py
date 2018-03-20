"""JobWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Loads jobs as first page
    path('', include('Job.urls', namespace="jobs")),
    path('attachment/', include('Attachment.urls', namespace="attachments")),
    path('company/', include('Company.urls', namespace="companies")),
    path('user/', include('User.urls', namespace="users")),
    path('address/', include('Address.urls', namespace="addresses")),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    # Allows serving images when clicking on them
    urlpatterns.append(path('media/(<path>.*)', serve,
                            {'document_root': settings.MEDIA_ROOT}))
