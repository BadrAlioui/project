from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('store.urls')),
    path('', include('authenticate.urls')),
    path('contact/', views.contact, name = 'contact'), 


]

