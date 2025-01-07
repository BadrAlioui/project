from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('store/', include('store.urls')),
    path('auth/', include('authenticate.urls')),
    


]

