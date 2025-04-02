from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home_page'),
    path('product/',views.product_watch,name="watch_home_page"),
]
