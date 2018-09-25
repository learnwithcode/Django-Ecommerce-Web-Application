from django.views.generic import ListView
from django.shortcuts import render
from .models import Product
# Create your views here.

class ProductListView(ListView):
    template_name = 'products/list.html'
    queryset = Product.objects.all()
    def get_context_data(self):
        context = super(ProductListView, self).get_context_data()
        return context


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'products': queryset
    }
    return render(request, "products/list.html", context)
