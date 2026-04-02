from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('mfgproducts/', views.mfgproduct_list, name='mfgproduct_list'),
    path('mfgproducts/create/', views.mfgproduct_create, name='mfgproduct_create'),
    path('mfgproducts/<int:pk>/edit/', views.mfgproduct_edit, name='mfgproduct_edit'),
    path('mfgproducts/<int:pk>/delete/', views.mfgproduct_delete, name='mfgproduct_delete'),
    path('billofmaterials/', views.billofmaterial_list, name='billofmaterial_list'),
    path('billofmaterials/create/', views.billofmaterial_create, name='billofmaterial_create'),
    path('billofmaterials/<int:pk>/edit/', views.billofmaterial_edit, name='billofmaterial_edit'),
    path('billofmaterials/<int:pk>/delete/', views.billofmaterial_delete, name='billofmaterial_delete'),
    path('mfgworkorders/', views.mfgworkorder_list, name='mfgworkorder_list'),
    path('mfgworkorders/create/', views.mfgworkorder_create, name='mfgworkorder_create'),
    path('mfgworkorders/<int:pk>/edit/', views.mfgworkorder_edit, name='mfgworkorder_edit'),
    path('mfgworkorders/<int:pk>/delete/', views.mfgworkorder_delete, name='mfgworkorder_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
