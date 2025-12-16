# apps/hostels/forms.py
from django import forms
from .models import Hostel

class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = ['name', 'license_id', 'address', 'city', 'phone', 'email', 'capacity', 'status']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }
