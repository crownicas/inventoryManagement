
from sre_constants import SUCCESS
from django.http import HttpResponse
from .models import product
from .forms import productForm
#for search
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import product

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404


# Necesary for user accounts

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# test for products acounts



# Create your views here.

@login_required
def home(request):
    return render(request, 'paginas/home.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def information(request):
    return render(request, 'paginas/information.html')

@login_required
def data(request):
    count = product.objects.all().count()
    context = {
        'count': count,
    }
    return render(request, 'paginas/data.html', context)
   
@login_required
def products(request):
    products = product.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(products,5)
        products = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': products,
        'paginator': paginator
    }
    return render(request, 'products/index.html', data)

@login_required
def create(request):
    form = productForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'product created successfully')
        return redirect('products')
    return render(request, 'products/create.html', {'form': form})

@login_required    
def edit(request, id):
    products = product.objects.get(id=id)
    form = productForm(request.POST or None, request.FILES or None, instance=products)
    if form.is_valid() and request.method == 'POST':
        form.save()
        messages.success(request, 'product updated successfully')
        return redirect('products')
    return render(request, 'products/edit.html', {'form': form})

@login_required    
def delete(request, id):
    products = product.objects.get(id=id)
    products.delete()
    messages.success(request, 'product deleted successfully')
    return redirect('products')


@login_required
def search(request):
    search = request.GET.get('search')
    products = product.objects.filter( Q(name__icontains = search) | Q(category__icontains=search) | Q(location__icontains=search) | Q(id__contains=search)).order_by('-id').distinct()
    
    if search == '':
        return redirect('products')
    if products.count() == 0:
        messages.warning(request, 'No products found')
        return redirect('products')
        
    data = {
        'entity': products,
    }
    return render(request, 'products/index.html', data)



#its just a test


@login_required
def products_sold(request):
    products = product.objects.filter(sold=True).order_by('-id')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(products,5)
        products = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': products,
        'paginator': paginator
    }

    return render(request, 'products/index.html', data)

@login_required
def products_unsold(request):
    products = product.objects.filter(sold=False).order_by('-id')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(products,5)
        products = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': products,
        'paginator': paginator
    }
    
   
        
    return render(request, 'products/index.html', data)

@login_required
def products_date(request):
    products = product.objects.all().order_by('upload_date')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(products,5)
        products = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': products,
        'paginator': paginator
    }
    
    return render(request, 'products/index.html', data)

