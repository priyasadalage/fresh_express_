from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from B_home.views import delete,broadcastviewset
router=DefaultRouter()
router.register('broadcastviewset',broadcastviewset,basename='todo')
urlpatterns = [
    
    path('',home),
    path('filter',filter),
    path('delete/<str:uid>',delete, name='delete'),
]
urlpatterns += router.urls