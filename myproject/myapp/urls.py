from django.urls import path
from . import views

urlpatterns = [
    path('create-user/', views.create_user),  # Question 1: Synchronous
    path('create-user-thread/', views.create_user_thread),  # Question 2: Same Thread
    path('create-user-transaction/', views.create_user_with_transaction),  # Question 3: Same Transaction
]
