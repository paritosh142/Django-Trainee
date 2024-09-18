from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.


def create_user(request):
    user = User.objects.create(username="testuser")
    return HttpResponse(f"User {user.username} created, signal triggered.")
