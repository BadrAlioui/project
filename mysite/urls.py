from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('contact/', views.contact, name = 'contact')
]
