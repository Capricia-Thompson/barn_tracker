from django.urls import path
from . import views
urlpatterns = [
    path('', views.programs),
    path('new_horse', views.new_program),
    path('create_horse', views.create_program),
    path('<int:id>/edit_horse', views.edit_program),
    path('<int:id>/update', views.update_program),
]
