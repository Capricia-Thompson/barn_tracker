from django.urls import path
from . import views
urlpatterns = [
    path('', views.horses_main),
    path('new_horse', views.new_horse),
    path('create_horse', views.create_horse),
    path('<int:id>', views.horse_bio),
    path('<int:id>/edit_horse', views.edit_horse),
    path('<int:id>/update', views.update_horse),
]
