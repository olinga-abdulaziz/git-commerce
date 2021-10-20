from django.shortcuts import render
from django.views import generic
from .models import Product
from django.urls import reverse_lazy
# Create your views here.
def home(request):
    return render(request,'baseapp/home.html',{})

class ManageStock(generic.ListView):
    model=Product
    ordering='-id'
    context_object_name='products'
    template_name='baseapp/management.html'

class UpdateProduct(generic.UpdateView):
    model=Product
    fields='__all__'
    context_object_name='product'
    template_name='baseapp/editstock.html'
    success_url=reverse_lazy('manage')


def manageSearch(request):
    model=Product
    if request.method=='POST':
        srch=request.POST.get('search')
        if srch:
            productList=Product.objects.filter(products=srch)
            return productList
    return render(request,'baseapp/management.html',{'productList':productList})
            
            


def editstock(request):
    return render(request,'baseapp/editstock.html')

class Addnewstock(generic.CreateView):
    model=Product
    fields='__all__'
    template_name='baseapp/addnew.html'
    success_url=reverse_lazy('manage')
