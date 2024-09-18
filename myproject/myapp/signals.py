from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
import threading
import time

## Signal Handler for Question 1: Demonstrating synchronous execution

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print("Signal handler started.")
    time.sleep(5)  # Simulate long-running process
    print("Signal handler finished.")



## Signal Handler for Question 2: Demonstrating same thread execution
@receiver(post_save, sender=User)
def user_saved_thread_handler(sender, instance, **kwargs):
    current_thread = threading.current_thread()
    print(f"Signal handler running in thread: {current_thread.name}")
