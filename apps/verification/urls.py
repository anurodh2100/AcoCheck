from django.urls import path
from . import views

app_name = "verification"

urlpatterns = [
    path("pending/", views.pending_residents, name="pending"),

    # Add these
    path("verify-resident/<int:resident_id>/", views.verify_resident, name="verify_resident"),
    path("approve-hostel/<int:hostel_id>/", views.approve_hostel, name="approve_hostel"),
    path("reject-hostel/<int:hostel_id>/", views.reject_hostel, name="reject_hostel"),
]