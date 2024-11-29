from django.urls import path
from .views import *



urlpatterns = [
    path('chome',CustomerHomeView.as_view(),name='home'),
    path('plist/<str:cat>',ProductListView.as_view(),name='plist'),
    path('pdetail/<int:pid>',ProductDetailView.as_view(),name='pdetail'),
    path('acart/<int:id>',addToCart,name='acart'),
    path('cartlist',CartListView.as_view(),name='cartlist'),
    path('incqty/<int:id>',IncreaseQuantity,name='incQuantity'),
    path('decqty/<int:id>',DecreaseQuantity,name='decQuantity'),
    path('removeitem/<int:id>',deleteCartItem,name='delcart'),
    path('order/<int:id>',placeOrder,name='order'),
    path('orderlist',OrderListView.as_view(),name='lorder'),
    path('corder/<int:id>',cancellOrder,name='cancelorder'),
    path('searchproduct',searchproduct,name='search')




]