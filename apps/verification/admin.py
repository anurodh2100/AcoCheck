from django.contrib import admin
from .models import VerificationLog
@admin.register(VerificationLog)
class VerificationLogAdmin(admin.ModelAdmin):
    list_display = ('resident','verified_by','status','verified_at')
