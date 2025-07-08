from django.urls import path
from . import views

urlpatterns = [
    path('login', views.get_data),
    path('user/<int:id>', views.user_detail)
]
