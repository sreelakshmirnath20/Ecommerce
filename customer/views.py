from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView,ListView,CreateView,DetailView
from account.models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

# Create your views here.
# class CustomerHomeView(View):
#     def get(self,request):
#         return render(request,"home.html")

def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"Please login First!!")
            return redirect('log')
    return inner
decorators=[never_cache,signin_required]
    


@method_decorator(decorator=decorators,name='dispatch')
class CustomerHomeView(TemplateView):
    template_name="home.html"


@method_decorator(decorator=decorators,name='dispatch')
class ProductListView(ListView):
    template_name="productlist.html"
    queryset=Products.objects.all()
    context_object_name="products"
    def get_queryset(self):
        cat=self.kwargs.get('cat')
        self.request.session['category']=cat
        return self.queryset.filter(category=cat)

# class ProductListView(View):
#     template_name="productlist.html"
#     queryset=Products.objects.all()
#     context_object_name="products"
#     def get(self,request):
#         queryset=queryset
#         return render(request,self.template_name,{self.context_object_name:queryset})


def searchproduct(request,*args,**kwargs):
    keyword=request.POST['searchkey']
    cat=request.session9['category']
    if keyword:
        products=Products.objects.filter(title__icontains=keyword,category=cat)
        return render(request,"productlist.html",{"products":products})
    else:
        return redirect('plist',cat=cat)



@method_decorator(decorator=decorators,name='dispatch')
class ProductDetailView(DetailView):
    template_name="productDetails.html"
    queryset=Products.objects.all()
    context_object_name="product"
    pk_url_kwarg="pid"

decorators
def addToCart(request,*args,**kwargs):
    try:
        pid=kwargs.get('id')
        product=Products.objects.get(id=pid)
        user=request.user
        cartcheck=Cart.objects.filter(product=product,user=user).exists()
        if cartcheck:
            cartitem=Cart.objects.get(product=product,user=user)
            cartitem.quantity+=1
            cartitem.save()
            messages.success(request,"Cart item quantity increased!!")
            return redirect('home')
        else:
            Cart.objects.create(product=product,user=user)
            messages.success(request,f"{product.title}Added To cart!!")
            return redirect('home')
    except Exception as e:
        print(e)
        messages.warning(request,"Something went WRONG!!")
        return redirect('home')
    
@method_decorator(decorator=decorators,name='dispatch')   
class CartListView(ListView):
    template_name="cartlist.html"
    queryset=Cart.objects.all()
    context_object_name="carts"
    def get_queryset(self):
        qs=self.queryset.filter(user=self.request.user)
        return qs
decorators 
def IncreaseQuantity(request,*args,**kwrgs):
    try:
        cid=kwrgs.get('id')
        cart=Cart.objects.get(id=cid)
        cart.quantity+=1
        cart.save()
        return redirect('cartlist')
    except:
        messages.warning(request,"Something went wrong!!")
        return redirect('cartlist')
decorators
def DecreaseQuantity(request, *args, **kwargs):
    try:
        cid = kwargs.get('id')
        cart = Cart.objects.get(id=cid)
        if cart.quantity==1:
            cart.delete()
            return redirect('cartlist')
        else:
            cart.quantity-=1 
            cart.save()
            return redirect('cartlist')
            
    except:
        messages.warning(request, "Something went wrong!!")
        return redirect('cartlist')
decorators  
def deleteCartItem(request,*args,**kwargs):
    try:
        cid=kwargs.get('id')
        cart=Cart.objects.get(id=cid)
        cart.delete()
        messages.success(request,"Item removed from cart!!")
        return redirect('cartlist')
    except:
        messages.warning(request,"Something went wrong!!")
        return redirect('cartlist')
decorators
def placeOrder(request,**kwargs):
    try:
        cid=kwargs.get('id')
        cart=Cart.objects.get(id=cid)
        Order.objects.create(product=cart.product,user=request.user,quantity=cart.quantity)
        cart.delete()

        # send_mail

        subject="Egadgets Order Notification"
        msg=f"Order for {cart.product.title} is Placed!!"
        f_rom='lakshmirnathclt@gmail.com'
        to_id=request.user.email
        send_mail(subject,msg,f_rom,[to_id],fail_silently=True)


        messages.success(request,f'{cart.product.title}\'s Order placed!!')
        return redirect('cartlist')
    except:
        messages.warning(request,"Something went wrong!!")
        return redirect('cartlist')
@method_decorator(decorator=decorators,name='dispatch')  
class OrderListView(ListView):
    template_name="orderlist.html"
    queryset=Order.objects.all()
    context_object_name="orders"
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
decorators
def cancellOrder(request,**kwargs):
    try:
        oid=kwargs.get('id')
        order=Order.objects.get(id=oid)
        order.status="Cancelled"
        order.save()
        messages.success(request,"Order Cancelled!!")
        return redirect('orders')
    except:
        messages.warning(request,"Something went wrong!!")
        return redirect('orders')
        


