from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product


class ProductsListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "image", "category", "price", "created_at", "updated_at")
    success_url = reverse_lazy('catalog: products_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "image", "category", "price", "created_at", "updated_at")
    success_url = reverse_lazy('catalog: products_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog: products_list')
