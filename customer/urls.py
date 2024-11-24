from django.urls import path
from .views import *



urlpatterns = [
    path('chome',CustomerHomeView.as_view(),name='home'),
    path('plist/<str:cat>',ProductListView.as_view(),name='plist'),
    path('pdetail/<int:pid>',ProductDetailView.as_view(),name='pdetail'),
    path('acart/<int:id>',addToCart,name='acart')
]