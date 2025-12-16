# apps/residents/forms.py
from django import forms
from .models import Resident

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        # adjust to your Resident model fields
        fields = ['name', 'phone', 'email', 'id_proof_type', 'id_proof_number', 'permanent_address', 'hostel', 'status', 'photo']
        widgets = {
            'permanent_address': forms.Textarea(attrs={'rows':3}),
        }
