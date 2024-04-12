from django.shortcuts import render
from venta.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.db import transaction

@login_required
def cart_view(request):
    user = request.user
    welcome_message = ""

    if user.role == 'cliente':
        welcome_message = '¡Bienvenido {}!'.format(user.username)
    elif user.role == 'interno':
        welcome_message = '¡Bienvenido {}! Usted ha iniciado sesión como usuario interno.'.format(user.username)
    else:
        welcome_message = '¡Bienvenido {}!'.format(user.username)

    # Aquí puedes definir otros datos que quieras pasar a la plantilla
    # Por ejemplo, si necesitas pasar datos sobre los productos en el carrito

    context = {
        'welcome_message': welcome_message,
        # Agrega otros datos necesarios aquí
    }

    return render(request, 'cart.html', context)

def store(request):
    
    if request.user.is_authenticated:
        print("Entro por aqui")
        client = request.user
        try:
            invoice = Invoice.objects.get(client=client, complete=False)
        except Invoice.DoesNotExist:
            invoice = Invoice.objects.create(client=client, complete=False)
        # invoice, created = Invoice.objects.get_or_create(client=client, complete=False)
        # items = invoice.invoicedetail_set.all()
        cartItems = invoice.get_item_total
    else:
        # items = []
        invoice = {"get_item_total":0, "get_cart_total":0}
        cartItems = invoice['get_item_total']
    
    products = Product.objects.all()
    context = {'products': products, 'cartItems':cartItems}
    return render(request, 'tienda/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        client = request.user.id
        invoice, created = Invoice.objects.get_or_create(client=client, complete=False)
        items = invoice.invoicedetail_set.all()
        cartItems = invoice.get_item_total
    else:
        items = []
        invoice = {"get_item_total":0, "get_cart_total":0}
        cartItems = invoice['get_item_total']
    context = {"items":items, "invoice":invoice, 'cartItems':cartItems}
    return render(request, 'tienda/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        client = request.user.id
        invoice, created = Invoice.objects.get_or_create(client=client, complete=False)
        items = invoice.invoicedetail_set.all()
        cartItems = invoice.get_item_total
    else:
        items = []
        invoice = {"get_item_total":0, "get_cart_total":0}
        cartItems = invoice['get_item_total']
    context = {"items":items, "invoice":invoice, "user": request.user, 'cartItems':cartItems}
    return render(request, 'tienda/checkout.html', context)


def addItemToCart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    client = request.user.id
    product = Product.objects.get(id=productId)
    
    invoice, created = Invoice.objects.get_or_create(client=client, complete=False) 
    invoiceDetail, created = InvoiceDetail.objects.get_or_create(invoice=invoice, product=product)
    
    
    if invoiceDetail.quantity is not None:
        if action == 'add':
            invoiceDetail.quantity += 1
        elif action == 'remove':
            invoiceDetail.quantity -= 1
    else:
        invoiceDetail.quantity = 1


    invoiceDetail.save()
    
    if invoiceDetail.quantity == 0:
        invoiceDetail.delete()
        
    
    invoice.total = invoice.get_cart_total()
    invoice.quantityItems = invoice.get_item_total()
    
    invoice.save()
        
    return JsonResponse('Item was added', safe=False)

@transaction.atomic
def processOrder(request):
    client = request.user.id
    invoice = Invoice.objects.get(client=client, complete=False)
    print(f"Before save - Invoice complete: {invoice.complete}")
    invoice.complete = True
    invoice.save()
    print(f"After save - Invoice complete: {invoice.complete}")
    return JsonResponse('Complete', safe=False)
    