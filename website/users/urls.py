from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup,name='signup_page'),
    path('login/',views.login,name='login_page'),
]
