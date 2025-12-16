# apps/residents/urls.py
from django.urls import path
from . import views

app_name = "residents"

urlpatterns = [
    path("list/", views.resident_list, name="list"),
    path("add/", views.resident_add, name="add"),
    path("<int:pk>/", views.resident_detail, name="detail"),
    path("<int:pk>/edit/", views.resident_edit, name="edit"),
    path("<int:pk>/delete/", views.resident_delete, name="delete"),
]
