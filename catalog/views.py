from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductsListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(is_published=True).order_by('name')


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        form.instance.created_at = timezone.now().date()
        form.instance.updated_at = timezone.now().date()
        form.instance.views_counter = 0
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        form.instance.updated_at = timezone.now().date()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')
