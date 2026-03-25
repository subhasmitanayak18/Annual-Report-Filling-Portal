from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('chapter3/', views.chapter3_view, name='chapter3'),
    path('chapter4/', views.chapter4_view, name='chapter4'),
    path('chapter4/submitted/', views.chapter4_submitted_view, name='chapter4_submitted'),
    path('chapter5/', views.chapter5_view, name='chapter5'),
    path('chapter5/submitted/', views.chapter5_submitted_view, name='chapter5_submitted'),
    path('chapter6/', views.chapter6_view, name='chapter6'),
    path('chapter6/submitted/', views.chapter6_submitted_view, name='chapter6_submitted'),
    path('chapter7/', views.chapter7_view, name='chapter7'),
    path('chapter7/submitted/', views.chapter7_submitted_view, name='chapter7_submitted'),
    path('chapter8/', views.chapter8_view, name='chapter8'),
    path('chapter8/submitted/', views.chapter8_submitted_view, name='chapter8_submitted'),
    path('chapter9/', views.chapter9_view, name='chapter9'),
    path('chapter9/submitted/', views.chapter9_submitted_view, name='chapter9_submitted'),
    path('chapter10/', views.chapter10_view, name='chapter10'),
    path('chapter10/submitted/', views.chapter10_submitted_view, name='chapter10_submitted'),
    path('chapter11/', views.chapter11_view, name='chapter11'),
    path('chapter11/submitted/', views.chapter11_submitted_view, name='chapter11_submitted'),
    path('chapter12/', views.chapter12_view, name='chapter12'),
    path('chapter12/submitted/', views.chapter12_submitted_view, name='chapter12_submitted'),
    path('login/', views.login_view, name='login'),
]