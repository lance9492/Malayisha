from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem, ShippingAddress
from .forms import ShippingAddressForm

def home(request):
    return render(request, 'home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, status='Cart')
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    if not created:
        order_item.quantity += 1
        order_item.save()
    return redirect('cart')

@login_required
def cart(request):
    order, created = Order.objects.get_or_create(user=request.user, status='Cart')
    return render(request, 'store/cart.html', {'order': order})

@login_required
def checkout(request):
    try:
        order = Order.objects.get(user=request.user, status='Cart')
    except Order.DoesNotExist:
        return redirect('cart')

    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            shipping_address = form.save(commit=False)
            shipping_address.user = request.user
            shipping_address.order = order
            shipping_address.save()
            
            order.status = 'Placed'
            order.save()
            
            return redirect('order_confirmation')
    else:
        form = ShippingAddressForm()

    context = {
        'form': form,
        'order': order,
    }
    return render(request, 'store/checkout.html', context)

@login_required
def order_confirmation(request):
    try:
        order = Order.objects.get(user=request.user, status='Placed')
    except Order.DoesNotExist:
        return redirect('store')

    context = {
        'order': order,
    }
    return render(request, 'store/order_confirmation.html', context)