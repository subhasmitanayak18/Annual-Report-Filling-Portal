from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('chapter3/', views.chapter3_view, name='chapter3'),
    path('chapter5/', views.chapter5_view, name='chapter5'),
    path('chapter4/', views.chapter4_view, name='chapter4'),
    path('chapter6/', views.chapter6_view, name='chapter6'),
    path('chapter7/', views.chapter7_view, name='chapter7'),
    path('chapter8/', views.chapter8_view, name='chapter8'),
    path('chapter9/', views.chapter9_view, name='chapter9'),
    path('chapter10/', views.chapter10_view, name='chapter10'),
    path('chapter11/', views.chapter11_view, name='chapter11'),
    path('chapter12/', views.chapter12_view, name='chapter12'),
    path('login/', views.login_view, name='login'),

]