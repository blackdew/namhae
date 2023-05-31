from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('<chapter>/<key>/', views.mission),
]
