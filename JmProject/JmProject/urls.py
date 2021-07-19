from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from JmApp import views as j 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', j.home, name='home'),
    path('JmApp/', include('JmApp.urls')),
    path('account/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)