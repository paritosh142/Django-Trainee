# Solutions to Django and Python Tasks

This repository contains solutions to the questions related to Django Signals and Python custom classes as required for the Django Trainee role at AccuKnox.

---

## 1. Django Signals

### Question 1: By default, are Django signals executed synchronously or asynchronously?
**Answer**: By default, Django signals are executed synchronously. This means that the signal is triggered and executed before the next line of code in the caller function is run.

- [Solution for Question 1: Synchronous or Asynchronous](myproject/myapp/signals.py)
  
#### Code:
```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(5)  # Simulate a delay
    print("Signal handler finished")

# The view triggering this signal is create_user
def create_user(request):
    user = User.objects.create(username="testuser_sync")
    return HttpResponse(f"User {user.username} created.")
```
#### Result:
```
Signal handler started
Signal handler finished
User save operation finished
```

### Question 2: Do Django signals run in the same thread as the caller?
**Answer**: Yes, Django signals run in the same thread as the caller by default. This can be verified by comparing thread IDs between the signal and the caller.

- [Solution for Question 2: Same Thread](myproject/myapp/signals.py)

#### Code:
```python
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

@receiver(post_save, sender=User)
def user_saved_thread_handler(sender, instance, **kwargs):
    current_thread = threading.current_thread()
    print(f"Signal handler running in thread: {current_thread.name}")

# The view triggering this signal is create_user_thread
def create_user_thread(request):
    current_thread = threading.current_thread()
    print(f"View running in thread: {current_thread.name}")
    user = User.objects.create(username="testuser_thread")
    return HttpResponse(f"User {user.username} created in thread.")

```
#### Result:
```
View running in thread: MainThread
Signal handler running in thread: MainThread
```
This confirms that Django signals run in the same thread as the caller. The thread ID remains the same throughout the process

### Question 3: By default, do Django signals run in the same database transaction as the caller?
**Answer**: Yes, Django signals run in the same database transaction as the caller by default. This means if the caller's transaction fails, the actions taken by the signal handlers will also be rolled back.

- [Solution for Question 3: Same Database Transaction](myproject/myapp/signals.py)

#### Code:
```python
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

@receiver(post_save, sender=User)
def user_saved_transaction_handler(sender, instance, **kwargs):
    print("Signal handler executed")

# The view triggering this signal is create_user_with_transaction
def create_user_with_transaction(request):
    try:
        with transaction.atomic():
            user = User.objects.create(username="transactionuser")
            raise Exception("Rolling back the transaction")
    except:
        return HttpResponse("Transaction rolled back, user not created.")
```
#### Result:
```
Signal handler executed
Transaction failed: Something went wrong!
Transaction complete
```
This confirms that Django signals are executed within the same database transaction by default. If the transaction fails, the signal handler's work is also rolled back.

---

## 2. Custom Python Classes

### Task: Create a Rectangle class with the following requirements:
1. An instance of the Rectangle class requires `length: int` and `width: int` to be initialized.
2. We can iterate over an instance of the Rectangle class.
3. When an instance of the Rectangle class is iterated over, we first get its length in the format: `{'length': <VALUE_OF_LENGTH>}` followed by its width `{'width': <VALUE_OF_WIDTH>}`.

- [Solution for Rectangle Class](myproject/myapp/rectangle.py)

#### Code:
```python
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Test the Rectangle class
if __name__ == "__main__":
    rect = Rectangle(5, 3)
    for dimension in rect:
        print(dimension)
```
#### Result:
```
{'length': 5}
{'width': 3}
```

---

### How to Run the Code
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```
2. Set up the Django project:
   - Ensure Django is installed: ```pip install django```
   - Run migrations: ```python manage.py migrate```
   
3. Access the signal demonstration views:
   - ```/myapp/create-user/```: Demonstrates synchronous signal execution.
   - ```/myapp/create-user-thread/```: Demonstrates signal running in the same thread as the caller.
   - ```/myapp/create-user-transaction/```: Demonstrates signal within the same database transaction.
