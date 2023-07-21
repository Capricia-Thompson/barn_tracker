from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('reg', views.reg_form),
    path('create_user', views.create_user),
    path('dash', views.dash),
    path('login', views.login),
    path('edit_user', views.edit_user),
    path('logout', views.logout)
]
