from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

#user accounts
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', views.home, name='home'),
    path('information', views.information, name='information'),
    path('data', views.data, name='data'),
    path('products', views.products, name='products'),
    path('product/create', views.create, name='create'),
    path('product/edit', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('product/edit/<int:id>', views.edit, name='edit'),
    path('product/search', views.search, name='search'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('logout', views.logout_view, name='logout'),
    
    
    #show products sold
    path('products/sold', views.products_sold, name='products_sold'),
    
    #show products unsold
    path('products/unsold', views.products_unsold, name='products_unsold'),
    
    #order products by date
    path('products/date', views.products_date, name='products_date'),
   
    
    
   

    
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)