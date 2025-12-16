from django.db import models
from apps.residents.models import Resident
from apps.accounts.models import User

class VerificationLog(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    verified_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    remarks = models.TextField(blank=True)
    def __str__(self): return f"{self.resident.full_name} - {self.status}"