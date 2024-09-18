import threading
from django.http import HttpResponse
from .models import User
from django.db import transaction


## View for testing synchronous execution (Question 1)
def create_user(request):
    user = User.objects.create(username="Test_User")
    return HttpResponse(f"User {user.username} created.")



## View for testing signal in the same thread (Question 2)
def create_user_thread(request):
    current_thread = threading.current_thread()
    print(f"View running in thread: {current_thread.name}")
    user = User.objects.create(username="Test_User_Thread")
    return HttpResponse(f"User {user.username} created in thread.")




## View for testing signal in the same database transaction (Question 3)
def create_user_with_transaction(request):
    try:
        with transaction.atomic():
            user = User.objects.create(username="Transaction_User")
            raise Exception("Rolling back the transaction")
    except:
        return HttpResponse("Transaction rolled back, user not created.")
