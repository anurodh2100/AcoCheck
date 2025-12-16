# apps/hostels/urls.py
from django.urls import path
from . import views

app_name = "hostels"

urlpatterns = [
    path("", views.hostel_list, name="list"),                # /hostels/
    path("dashboard/", views.hostel_dashboard, name="dashboard"),
    path("add/", views.hostel_add, name="add"),
    path("<int:pk>/", views.hostel_detail, name="detail"),
    path("<int:pk>/edit/", views.hostel_edit, name="edit"),
    path("<int:pk>/delete/", views.hostel_delete, name="delete"),
]
