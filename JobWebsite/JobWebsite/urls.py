from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.static import serve

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
