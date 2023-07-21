from django.urls import path
from . import views
urlpatterns = [
    path('cust_dash', views.view_cust),
]
