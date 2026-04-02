from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import MFGProduct, BillOfMaterial, MFGWorkOrder
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusMfg with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusmfg.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if MFGProduct.objects.count() == 0:
            for i in range(10):
                MFGProduct.objects.create(
                    name=f"Sample MFGProduct {i+1}",
                    sku=f"Sample {i+1}",
                    category=f"Sample {i+1}",
                    unit_cost=round(random.uniform(1000, 50000), 2),
                    selling_price=round(random.uniform(1000, 50000), 2),
                    stock=random.randint(1, 100),
                    min_stock=random.randint(1, 100),
                    status=random.choice(["active", "discontinued"]),
                    lead_time_days=random.randint(1, 100),
                )
            self.stdout.write(self.style.SUCCESS('10 MFGProduct records created'))

        if BillOfMaterial.objects.count() == 0:
            for i in range(10):
                BillOfMaterial.objects.create(
                    product_name=f"Sample BillOfMaterial {i+1}",
                    component=f"Sample {i+1}",
                    quantity=random.randint(1, 100),
                    unit=f"Sample {i+1}",
                    unit_cost=round(random.uniform(1000, 50000), 2),
                    total_cost=round(random.uniform(1000, 50000), 2),
                    supplier=["TechVision Pvt Ltd","Global Solutions","Pinnacle Systems","Nova Enterprises","CloudNine Solutions","MetaForge Inc","DataPulse Analytics","QuantumLeap Tech","SkyBridge Corp","Zenith Innovations"][i],
                    status=random.choice(["active", "obsolete"]),
                )
            self.stdout.write(self.style.SUCCESS('10 BillOfMaterial records created'))

        if MFGWorkOrder.objects.count() == 0:
            for i in range(10):
                MFGWorkOrder.objects.create(
                    wo_number=f"Sample {i+1}",
                    product_name=f"Sample MFGWorkOrder {i+1}",
                    quantity=random.randint(1, 100),
                    status=random.choice(["planned", "in_production", "quality_check", "completed", "cancelled"]),
                    start_date=date.today() - timedelta(days=random.randint(0, 90)),
                    due_date=date.today() - timedelta(days=random.randint(0, 90)),
                    assigned_to=f"Sample {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 MFGWorkOrder records created'))
