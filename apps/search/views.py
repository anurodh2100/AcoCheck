from django.shortcuts import render
from apps.residents.models import Resident
from apps.hostels.models import Hostel
from apps.verification.models import VerificationLog

def search_all(request):
    query = request.GET.get("q", "").strip()
    
    residents = hostels = logs = []

    if query:
        residents = Resident.objects.filter(
            name__icontains=query
        ) | Resident.objects.filter(
            id_proof_number__icontains=query
        )

        hostels = Hostel.objects.filter(
            name__icontains=query
        ) | Hostel.objects.filter(
            license_id__icontains=query
        )

        logs = VerificationLog.objects.filter(
            resident__name__icontains=query
        ) | VerificationLog.objects.filter(
            status__icontains=query
        )

    context = {
        "query": query,
        "residents": residents,
        "hostels": hostels,
        "logs": logs
    }

    return render(request, "search/results.html", context)
