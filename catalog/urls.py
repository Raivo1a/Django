from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductsListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ProductsByCategoryView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='products_detail'),
    path('products/create', ProductCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='products_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='products_delete'),
    path('category/<int:pk>/products/', ProductsByCategoryView.as_view(), name='products_by_category'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
