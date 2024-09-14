from django.urls import path,include 
from .views import index
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns

urlpatterns = [
    path('',index,name = 'index')
]