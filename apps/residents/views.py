# apps/residents/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Resident
from .forms import ResidentForm

@login_required
def resident_list(request):
    if request.user.role != 'owner':
        return render(request,'errors/403.html')
    residents = Resident.objects.filter(hostel__owner=request.user)
    return render(request,'residents/list.html',{'residents':residents})

@login_required
def resident_detail(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    return render(request,'residents/detail.html',{'resident':resident})

@login_required
def resident_add(request):
    if request.user.role != 'owner':
        return render(request,'errors/403.html')
    if request.method == 'POST':
        form = ResidentForm(request.POST, request.FILES)
        if form.is_valid():
            r = form.save(commit=False)
            # set hostel if provided in form or logic to set default
            r.save()
            return redirect('residents:list')
    else:
        form = ResidentForm()
    return render(request,'residents/form.html',{'form': form, 'action': 'Add'})

@login_required
def resident_edit(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    if request.method == 'POST':
        form = ResidentForm(request.POST, request.FILES, instance=resident)
        if form.is_valid():
            form.save()
            return redirect('residents:list')
    else:
        form = ResidentForm(instance=resident)
    return render(request,'residents/form.html',{'form': form, 'action': 'Edit', 'resident': resident})

@login_required
def resident_delete(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    if request.method == 'POST':
        resident.delete()
        return redirect('residents:list')
    return render(request,'residents/confirm_delete.html',{'resident': resident})
