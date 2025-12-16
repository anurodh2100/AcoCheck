from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.hostels.models import Hostel
from apps.residents.models import Resident
from apps.verification.models import VerificationLog

@login_required
def dashboard_home(request):
    role = request.user.role
    context = {}

    # =========================
    # OWNER DASHBOARD
    # =========================
    if role == 'owner':
        hostels = Hostel.objects.filter(owner=request.user)

        # FULL queryset for counts
        all_residents = Resident.objects.filter(
            hostel__owner=request.user
        ).order_by('-created_at')

        # Slice ONLY for recent display
        recent_residents = all_residents[:5]

        # Counts from full queryset
        pending = all_residents.filter(status='added').count()
        approved = all_residents.filter(status='verified').count()
        rejected = all_residents.filter(status='rejected').count()

        context.update({
            'hostels': hostels,
            'recent_residents': recent_residents,
            'pending': pending,
            'approved': approved,
            'rejected': rejected,
        })

        return render(request, 'dashboard/owner_dashboard.html', context)

    # =========================
    # POLICE DASHBOARD
    # =========================
    if role == 'police':

        pending_hostels = Hostel.objects.filter(status='pending')
        pending_residents = Resident.objects.filter(status='added')
        recent_logs = VerificationLog.objects.order_by('-verified_at')[:10]

        context.update({
            'pending_hostels': pending_hostels,
            'pending_residents': pending_residents,
            'recent_logs': recent_logs,
        })

        return render(request, 'dashboard/police_dashboard.html', context)

    # =========================
    # ADMIN DASHBOARD
    # =========================
    return render(request, 'dashboard/admin_dashboard.html')
