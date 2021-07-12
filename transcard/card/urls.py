from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('list/', views.card, name="list"),
    path('ready_inn/', views.check_inn, name="ready_inn"),
    path('generate_loadout/', views.generate_loadout, name='loadout_generate'),
]
