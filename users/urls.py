from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.email_login_view, name='login'),
    path('index/', views.index_view, name='index')
]
