# apps/hostels/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Hostel
from .forms import HostelForm

@login_required
def hostel_dashboard(request):
    if request.user.role != 'owner':
        return render(request, 'errors/403.html')
    hostels = Hostel.objects.filter(owner=request.user)
    return render(request, 'hostels/list.html', {'hostels': hostels})

@login_required
def hostel_list(request):
    if request.user.role != 'owner':
        return render(request, 'errors/403.html')
    hostels = Hostel.objects.filter(owner=request.user)
    return render(request, 'hostels/list.html', {'hostels': hostels})

@login_required
def hostel_detail(request, pk):
    hostel = get_object_or_404(Hostel, pk=pk)
    # permission: owner or admin
    if request.user.role == 'owner' and hostel.owner != request.user:
        return render(request, 'errors/403.html')
    return render(request, 'hostels/detail.html', {'hostel': hostel})

@login_required
def hostel_add(request):
    if request.user.role != 'owner':
        return render(request, 'errors/403.html')
    if request.method == 'POST':
        form = HostelForm(request.POST, request.FILES)
        if form.is_valid():
            h = form.save(commit=False)
            h.owner = request.user
            h.save()
            return redirect('hostels:dashboard')
    else:
        form = HostelForm()
        return render(request, 'hostels/form.html', {'form': form, 'action': 'Add'})


@login_required
def hostel_edit(request, pk):
    hostel = get_object_or_404(Hostel, pk=pk)
    if request.user.role != 'owner' or hostel.owner != request.user:
        return render(request, 'errors/403.html')
    if request.method == 'POST':
        form = HostelForm(request.POST, request.FILES, instance=hostel)
        if form.is_valid():
            form.save()
            return redirect('hostels:dashboard')
    else:
        form = HostelForm(instance=hostel)
    return render(request, 'hostels/form.html', {'form': form, 'action': 'Edit', 'hostel': hostel})

@login_required
def hostel_delete(request, pk):
    hostel = get_object_or_404(Hostel, pk=pk)
    if request.user.role != 'owner' or hostel.owner != request.user:
        return render(request, 'errors/403.html')
    if request.method == 'POST':
        hostel.delete()
        return redirect('hostels:dashboard')
    return render(request, 'hostels/confirm_delete.html', {'hostel': hostel})
