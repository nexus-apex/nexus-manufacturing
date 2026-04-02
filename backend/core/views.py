import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import MFGProduct, BillOfMaterial, MFGWorkOrder


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['mfgproduct_count'] = MFGProduct.objects.count()
    ctx['mfgproduct_active'] = MFGProduct.objects.filter(status='active').count()
    ctx['mfgproduct_discontinued'] = MFGProduct.objects.filter(status='discontinued').count()
    ctx['mfgproduct_total_unit_cost'] = MFGProduct.objects.aggregate(t=Sum('unit_cost'))['t'] or 0
    ctx['billofmaterial_count'] = BillOfMaterial.objects.count()
    ctx['billofmaterial_active'] = BillOfMaterial.objects.filter(status='active').count()
    ctx['billofmaterial_obsolete'] = BillOfMaterial.objects.filter(status='obsolete').count()
    ctx['billofmaterial_total_unit_cost'] = BillOfMaterial.objects.aggregate(t=Sum('unit_cost'))['t'] or 0
    ctx['mfgworkorder_count'] = MFGWorkOrder.objects.count()
    ctx['mfgworkorder_planned'] = MFGWorkOrder.objects.filter(status='planned').count()
    ctx['mfgworkorder_in_production'] = MFGWorkOrder.objects.filter(status='in_production').count()
    ctx['mfgworkorder_quality_check'] = MFGWorkOrder.objects.filter(status='quality_check').count()
    ctx['recent'] = MFGProduct.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def mfgproduct_list(request):
    qs = MFGProduct.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'mfgproduct_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def mfgproduct_create(request):
    if request.method == 'POST':
        obj = MFGProduct()
        obj.name = request.POST.get('name', '')
        obj.sku = request.POST.get('sku', '')
        obj.category = request.POST.get('category', '')
        obj.unit_cost = request.POST.get('unit_cost') or 0
        obj.selling_price = request.POST.get('selling_price') or 0
        obj.stock = request.POST.get('stock') or 0
        obj.min_stock = request.POST.get('min_stock') or 0
        obj.status = request.POST.get('status', '')
        obj.lead_time_days = request.POST.get('lead_time_days') or 0
        obj.save()
        return redirect('/mfgproducts/')
    return render(request, 'mfgproduct_form.html', {'editing': False})


@login_required
def mfgproduct_edit(request, pk):
    obj = get_object_or_404(MFGProduct, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.sku = request.POST.get('sku', '')
        obj.category = request.POST.get('category', '')
        obj.unit_cost = request.POST.get('unit_cost') or 0
        obj.selling_price = request.POST.get('selling_price') or 0
        obj.stock = request.POST.get('stock') or 0
        obj.min_stock = request.POST.get('min_stock') or 0
        obj.status = request.POST.get('status', '')
        obj.lead_time_days = request.POST.get('lead_time_days') or 0
        obj.save()
        return redirect('/mfgproducts/')
    return render(request, 'mfgproduct_form.html', {'record': obj, 'editing': True})


@login_required
def mfgproduct_delete(request, pk):
    obj = get_object_or_404(MFGProduct, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/mfgproducts/')


@login_required
def billofmaterial_list(request):
    qs = BillOfMaterial.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(product_name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'billofmaterial_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def billofmaterial_create(request):
    if request.method == 'POST':
        obj = BillOfMaterial()
        obj.product_name = request.POST.get('product_name', '')
        obj.component = request.POST.get('component', '')
        obj.quantity = request.POST.get('quantity') or 0
        obj.unit = request.POST.get('unit', '')
        obj.unit_cost = request.POST.get('unit_cost') or 0
        obj.total_cost = request.POST.get('total_cost') or 0
        obj.supplier = request.POST.get('supplier', '')
        obj.status = request.POST.get('status', '')
        obj.save()
        return redirect('/billofmaterials/')
    return render(request, 'billofmaterial_form.html', {'editing': False})


@login_required
def billofmaterial_edit(request, pk):
    obj = get_object_or_404(BillOfMaterial, pk=pk)
    if request.method == 'POST':
        obj.product_name = request.POST.get('product_name', '')
        obj.component = request.POST.get('component', '')
        obj.quantity = request.POST.get('quantity') or 0
        obj.unit = request.POST.get('unit', '')
        obj.unit_cost = request.POST.get('unit_cost') or 0
        obj.total_cost = request.POST.get('total_cost') or 0
        obj.supplier = request.POST.get('supplier', '')
        obj.status = request.POST.get('status', '')
        obj.save()
        return redirect('/billofmaterials/')
    return render(request, 'billofmaterial_form.html', {'record': obj, 'editing': True})


@login_required
def billofmaterial_delete(request, pk):
    obj = get_object_or_404(BillOfMaterial, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/billofmaterials/')


@login_required
def mfgworkorder_list(request):
    qs = MFGWorkOrder.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(wo_number__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'mfgworkorder_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def mfgworkorder_create(request):
    if request.method == 'POST':
        obj = MFGWorkOrder()
        obj.wo_number = request.POST.get('wo_number', '')
        obj.product_name = request.POST.get('product_name', '')
        obj.quantity = request.POST.get('quantity') or 0
        obj.status = request.POST.get('status', '')
        obj.start_date = request.POST.get('start_date') or None
        obj.due_date = request.POST.get('due_date') or None
        obj.assigned_to = request.POST.get('assigned_to', '')
        obj.save()
        return redirect('/mfgworkorders/')
    return render(request, 'mfgworkorder_form.html', {'editing': False})


@login_required
def mfgworkorder_edit(request, pk):
    obj = get_object_or_404(MFGWorkOrder, pk=pk)
    if request.method == 'POST':
        obj.wo_number = request.POST.get('wo_number', '')
        obj.product_name = request.POST.get('product_name', '')
        obj.quantity = request.POST.get('quantity') or 0
        obj.status = request.POST.get('status', '')
        obj.start_date = request.POST.get('start_date') or None
        obj.due_date = request.POST.get('due_date') or None
        obj.assigned_to = request.POST.get('assigned_to', '')
        obj.save()
        return redirect('/mfgworkorders/')
    return render(request, 'mfgworkorder_form.html', {'record': obj, 'editing': True})


@login_required
def mfgworkorder_delete(request, pk):
    obj = get_object_or_404(MFGWorkOrder, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/mfgworkorders/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['mfgproduct_count'] = MFGProduct.objects.count()
    data['billofmaterial_count'] = BillOfMaterial.objects.count()
    data['mfgworkorder_count'] = MFGWorkOrder.objects.count()
    return JsonResponse(data)
