from django.contrib import admin
from .models import MFGProduct, BillOfMaterial, MFGWorkOrder

@admin.register(MFGProduct)
class MFGProductAdmin(admin.ModelAdmin):
    list_display = ["name", "sku", "category", "unit_cost", "selling_price", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "sku", "category"]

@admin.register(BillOfMaterial)
class BillOfMaterialAdmin(admin.ModelAdmin):
    list_display = ["product_name", "component", "quantity", "unit", "unit_cost", "created_at"]
    list_filter = ["status"]
    search_fields = ["product_name", "component", "unit"]

@admin.register(MFGWorkOrder)
class MFGWorkOrderAdmin(admin.ModelAdmin):
    list_display = ["wo_number", "product_name", "quantity", "status", "start_date", "created_at"]
    list_filter = ["status"]
    search_fields = ["wo_number", "product_name", "assigned_to"]
