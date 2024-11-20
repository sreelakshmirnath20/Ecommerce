from django.urls import path
from .views import *


urlpatterns = [
    path('chome',CustomerHomeView.as_view(),name='home'),
]