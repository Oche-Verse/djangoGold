from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.index, name='index'),
    path('forex1', views.forex1, name='forex1'),
    path('forex2', views.forex2, name='forex2'),
    path('forexDetail', views.forexDetail, name='forexDetail'),
    path('gedmentor', views.gedmentor, name='gedmentor'),
    path('gedSchool', views.gedSchool, name='gedSchool'),
    path('speakmentor', views.speakmentor, name='speakmentor'),
    path('stage3', views.stage3, name='stage3'),
    
    





    
]