# apps/accounts/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.hostels.models import Hostel
from apps.residents.models import Resident
import random, datetime

User = get_user_model()

class Command(BaseCommand):
    help = "Seed demo users, hostels, and residents"

    def handle(self, *args, **options):
        self.stdout.write("🟦 Seeding Data...")

        # users: create only if not exists
        users = [
            {'username': 'owner1', 'password': 'owner123', 'role': 'owner'},
            {'username': 'police1', 'password': 'police123', 'role': 'police'},
            {'username': 'admin1', 'password': 'admin123', 'role': 'admin'},
        ]
        for u in users:
            user, created = User.objects.get_or_create(username=u['username'], defaults={'role': u['role']})
            if created:
                user.set_password(u['password'])
                user.save()
        self.stdout.write("✔ Users created/ensured")

        # hostels: ensure existence and license uniqueness
        owner = User.objects.filter(username='owner1').first()
        if owner:
            hostels = [
                {'name': 'Elite PG Bangalore', 'license_id': 'LIC001/2025', 'address': '123 MG Road', 'city':'Bangalore', 'phone':'+919876543210', 'email':'rajesh@elitepg.com', 'capacity': 50, 'status': 'approved'},
            ]
            for h in hostels:
                hostel, created = Hostel.objects.get_or_create(license_id=h['license_id'], defaults={
                    'owner': owner,
                    'name': h['name'],
                    'address': h['address'],
                    'city': h['city'],
                    'phone': h['phone'],
                    'email': h['email'],
                    'capacity': h['capacity'],
                    'status': h['status']
                })
        self.stdout.write("✔ Hostels created/ensured")

        # residents: create example residents for that hostel
        hostel = Hostel.objects.filter(owner=owner).first()
        if hostel:
            demo_residents = [
                {'name':'Akshay Singh', 'phone': '+91-9000000001', 'id_proof_type':'Aadhar', 'id_proof_number':'XXXX-XXXX-1234', 'status':'approved'},
                {'name':'Vikram Desai', 'phone': '+91-9000000002', 'id_proof_type':'License', 'id_proof_number':'DL-0001-2020', 'status':'verified'},
                {'name':'Rahul Verma', 'phone': '+91-9000000003', 'id_proof_type':'PAN', 'id_proof_number':'ABCDE1234F', 'status':'rejected'},
            ]
            for r in demo_residents:
                Resident.objects.get_or_create(
                    id_proof_number = r['id_proof_number'],
                    defaults = {
                        'name': r['name'],
                        'phone': r['phone'],
                        'id_proof_type': r['id_proof_type'],
                        'hostel': hostel,
                        'status': r['status']
                    }
                )

        self.stdout.write("✔ Residents created/ensured")
        self.stdout.write("✅ Done.")
