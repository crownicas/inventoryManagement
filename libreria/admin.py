from django.contrib import admin
from .models import product

# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description', 
        'location', 
        'purchase_cost',
        'sale_cost', 
        'upload_date',
        'sale_date', 
        'imagen' , 
        'intermediary_cost',
        'profit', 
        'sold', 
        'category'
        )
    
    list_filter = (
        'location',
        'sold',
        'upload_date',
        'sale_date', 
        'category', 
        'intermediary_cost'
        )
    
    search_fields = (
        'id', 
        'name', 
        'description', 
        'location', 
        'sold')
    
    
    list_per_page = 10
    
admin.site.register(product, productAdmin)

