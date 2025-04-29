from django.urls import path
from calcuvaca_site import views

urlpatterns = [
    path('', views.home, name="home"),
]