from django.urls import path,include

from .views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('broadcastviewset',broadcastviewset,basename='todo')


urlpatterns = [
    
    # path('',home),
    path('delete/<str:uid>',delete, name='delete'),
]


urlpatterns += router.urls