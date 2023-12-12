from django.urls import path
from . import views

app_name = 'gimnasio'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('fighters/', views.fighters, name='fighters'),
    # path('events/', views.events, name='events'),
    # Add similar paths for other views (e.g., about, news, contact, etc.)
]
