from django.urls import path
from calcuvaca_site import views

urlpatterns = [
    path('', views.home, name="home"),
    path('employ/insert', views.employ_insert, name="employ_insert"),
    path('employ/<str:id>', views.employ_details, name="details"),
    path('employ/<str:id>/take-vacation', views.vacation_taken_insert, name="vacation_taken_insert"),
]
