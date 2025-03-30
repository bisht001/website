from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup,name='signup_page'),
    path('signup_func/',views.signup_func,name='signup_func'),
    path('login/',views.login,name='login_page'),
    path('login_func/',views.login_func,name='login_func'),
    path('logout/',views.logout,name='logout_page'),
]
