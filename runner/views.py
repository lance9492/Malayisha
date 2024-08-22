from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ErrandRequestForm
from .models import RunnerService

@login_required
def runner_service(request):
    if request.method == 'POST':
        form = ErrandRequestForm(request.POST)
        if form.is_valid():
            errand = form.save(commit=False)
            errand.user = request.user
            errand.save()
            return redirect('errand_confirmation')
    else:
        form = ErrandRequestForm()
    services = RunnerService.objects.all()
    return render(request, 'runner/runner_service.html', {'form': form, 'services': services})

@login_required
def errand_confirmation(request):
    return render(request, 'runner/errand_confirmation.html')