from django.urls import path
from . import views

urlpatterns = [
    path('watch/<str:brand>/<int:myid>/', views.product_watch, name="watch")
]

