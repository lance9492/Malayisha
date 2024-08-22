from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DeliveryRequestForm
from .models import Delivery

@login_required
def courier_service(request):
    if request.method == 'POST':
        form = DeliveryRequestForm(request.POST)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.order = request.user.order_set.filter(status='Cart').first()
            delivery.save()
            return redirect('delivery_confirmation')
    else:
        form = DeliveryRequestForm()
    return render(request, 'courier/courier_service.html', {'form': form})

@login_required
def delivery_confirmation(request):
    return render(request, 'courier/delivery_confirmation.html')