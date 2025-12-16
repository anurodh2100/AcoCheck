from django.contrib import admin
from .models import Resident, ResidentDocument
@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ('name','hostel','id_proof_type','status','created_at')
@admin.register(ResidentDocument)
class ResidentDocumentAdmin(admin.ModelAdmin):
    list_display = ('resident','doc_type','uploaded_at')
