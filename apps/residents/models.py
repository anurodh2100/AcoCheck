from django.db import models
from apps.hostels.models import Hostel

class Resident(models.Model):
    STATUS_CHOICES = [('added','Added'),('verified','Verified'),('approved','Approved'),('rejected','Rejected')]
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='residents')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    id_proof_type = models.CharField(max_length=50)
    id_proof_number = models.CharField(max_length=100)
    permanent_address = models.TextField()
    photo = models.ImageField(upload_to='resident_photos/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='added')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return self.name

class ResidentDocument(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='documents')
    doc_type = models.CharField(max_length=100)
    document = models.FileField(upload_to='resident_docs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.resident.name} - {self.doc_type}"
