from django.urls import path

from . import views

app_name = 'sports'
urlpatterns = [
    path('', views.index, name='index'),
    path('rules/', views.rules, name='rules'),
    path('notables/', views.notables, name='notables'),
    path('notables/<int:player_id>/', views.detail, name='detail'),
    path('external/', views.external, name='external'),
]