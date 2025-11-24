from django.urls import path
from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing_page.html')

def product_details(request, product_id):
    return render(request, 'product_details.html', {'product_id': product_id})

def basket_management(request):
    return render(request, 'basket_management.html')

def checkout(request):
    return render(request, 'checkout.html')

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('product/<int:product_id>/', product_details, name='product_details'),
    path('basket/', basket_management, name='basket_management'),
    path('checkout/', checkout, name='checkout'),
]