from django.urls import path
from store.views import *

app_name = 'store'
urlpatterns = [
    path('', trang_chu, name='trang_chu'),
    # path('master/', master, name='master'),
    path('trang_chu_2/', trang_chu_2, name='trang_chu_2'),
    path('danh-muc/<int:pk>/', danh_muc, name='danh_muc'),
    path('lien-he/', lien_he, name='lien_he'),
    path('chi-tiet-san-pham/<int:pk>', chi_tiet_san_pham, name='chi_tiet_san_pham'),
    path('rss/', rss, name='rss'),
    path('tim-kiem/', tim_kiem, name='tim_kiem'),
    path('products-service/', products_service, name='products_service'),

]
