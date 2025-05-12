from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('index/', views.index, name='index'),
    path('predict/', views.predict_view, name='predict'),
    path('logout/', views.logout_view, name='logout'),
]

