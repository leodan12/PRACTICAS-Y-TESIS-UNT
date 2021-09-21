
from django.contrib import admin
#archivos
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('SeguridadApp.urls')),
    path('',include('AsesoresApp.urls')),
    path('',include('alumnoApp.urls')),
    path('',include('adminApp.urls')),

]

#archivos
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)