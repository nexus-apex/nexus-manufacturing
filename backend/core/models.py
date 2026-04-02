from django.db import models

class MFGProduct(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, blank=True, default="")
    category = models.CharField(max_length=255, blank=True, default="")
    unit_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    selling_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    stock = models.IntegerField(default=0)
    min_stock = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("discontinued", "Discontinued")], default="active")
    lead_time_days = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class BillOfMaterial(models.Model):
    product_name = models.CharField(max_length=255)
    component = models.CharField(max_length=255, blank=True, default="")
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=255, blank=True, default="")
    unit_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    supplier = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("obsolete", "Obsolete")], default="active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.product_name

class MFGWorkOrder(models.Model):
    wo_number = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255, blank=True, default="")
    quantity = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("planned", "Planned"), ("in_production", "In Production"), ("quality_check", "Quality Check"), ("completed", "Completed"), ("cancelled", "Cancelled")], default="planned")
    start_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    assigned_to = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.wo_number
