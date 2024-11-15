from django.urls import path
from .views import *

urlpatterns =[
    path('log',LoginView.as_view(),name='log')
]