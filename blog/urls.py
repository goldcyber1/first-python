from django.urls import path
from . import views

urlpatterns = [
    path('admin/list/', views.admin_list, name='admin_list'),
    
    path('', views.insp_list, name='insp_list'),
    path('insp/new/', views.insp_new, name='insp_new'),
    path('insp/<mba_cd>/<reptdc_no>/detail/', views.insp_detail, name='insp_detail'),
    path('insp/<mba_cd>/<reptdc_no>/edit/', views.insp_edit, name='insp_edit'),
    path('insp/<mba_cd>/<reptdc_no>/delete/', views.insp_delete, name='insp_delete'),
    
    
    path('admin/<user_id>/detail/', views.admin_detail, name='admin_detail'),
    path('admin/new/', views.admin_new, name='admin_new'),
    path('admin/<user_id>/edit/', views.admin_edit, name='admin_edit'),
]
