from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView,ListView,CreateView,DetailView
from account.models import *
from django.contrib import messages

# Create your views here.
# class CustomerHomeView(View):
#     def get(self,request):
#         return render(request,"home.html")

class CustomerHomeView(TemplateView):
    template_name="home.html"

class ProductListView(ListView):
    template_name="productlist.html"
    queryset=Products.objects.all()
    context_object_name="products"
    def get_queryset(self):
        cat=self.kwargs.get('cat')
        return self.queryset.filter(category=cat)

# class ProductListView(View):
#     template_name="productlist.html"
#     queryset=Products.objects.all()
#     context_object_name="products"
#     def get(self,request):
#         queryset=queryset
#         return render(request,self.template_name,{self.context_object_name:queryset})


class ProductDetailView(DetailView):
    template_name="productDetails.html"
    queryset=Products.objects.all()
    context_object_name="product"
    pk_url_kwarg="pid"

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
    
class CartListView(ListView):
    template_name="cartlist.html"


