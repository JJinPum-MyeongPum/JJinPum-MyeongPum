from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from JmApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('detail/<str:id>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('edit/<str:id>', views.edit, name='edit'),
    path('delete/<str:id>', views.delete, name='delete'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
