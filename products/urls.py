
from django.conf.urls import url
app_name = 'products'
from .views import (
        ProductListView, 
        product_list_view, 
        ProductDetailView, 
        product_detail_view,
        ProductDetailView, 
        product_detail_view,
        ProductFeaturedView,
        ProductFeaturedDetailView
        )

urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'^products/(?P<slug>[\w-]+)/', ProductDetailView.as_view(), name='product_detail'),
    # url(r'^products-fbv/$', product_list_view),
    # url(r'^products-fbv/(?P<pk>\d+)/', product_detail_view),
    # url(r'^featured/$', ProductFeaturedView.as_view()),
    # url(r'^featured/(?P<pk>\d+)/', ProductFeaturedDetailView.as_view()),
]
