from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from apps.residents.models import Resident
from apps.hostels.models import Hostel
from apps.verification.models import VerificationLog


# ------------------------------------
#  POLICE CHECK
# ------------------------------------
def is_police(user):
    return user.role == "police"


# ------------------------------------
#  PENDING RESIDENTS LIST
# ------------------------------------
@login_required
@user_passes_test(is_police)
def pending_residents(request):
    pending = Resident.objects.filter(status="added")
    return render(request, "verification/pending.html", {"residents": pending})


# ------------------------------------
#  APPROVE HOSTEL
#  (Hostel model does NOT have `is_approved`)
#  So we update:  status = "approved"
# ------------------------------------
@login_required
@user_passes_test(is_police)
def approve_hostel(request, hostel_id):
    hostel = get_object_or_404(Hostel, id=hostel_id)

    hostel.status = "approved"
    hostel.save()

    messages.success(request, "Hostel approved successfully.")
    return redirect("dashboard:home")


# ------------------------------------
#  REJECT HOSTEL
# ------------------------------------
@login_required
@user_passes_test(is_police)
def reject_hostel(request, hostel_id):
    hostel = get_object_or_404(Hostel, id=hostel_id)

    hostel.status = "rejected"
    hostel.save()

    messages.error(request, "Hostel rejected.")
    return redirect("dashboard:home")


# ------------------------------------
#  VERIFY RESIDENT
# ------------------------------------
@login_required
@user_passes_test(is_police)
def verify_resident(request, resident_id):
    resident = get_object_or_404(Resident, id=resident_id)

    resident.status = "verified"
    resident.save()

    # create log
    VerificationLog.objects.create(
        resident=resident,
        status="verified",
        verified_by=request.user
    )

    messages.success(request, "Resident verified successfully.")
    return redirect("dashboard:home")
