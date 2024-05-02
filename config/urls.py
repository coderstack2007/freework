from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('action/', include('myapp.urls') ),
    path('index2/', include('myapp.urls')),
    path('index3/', include('myapp.urls')),
    path('Sign/', include('myapp.urls')),
    path('copy/', include('myapp.urls') ),
    path('make/', include('myapp.urls')),
    path('account/', include('myapp.urls') )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)