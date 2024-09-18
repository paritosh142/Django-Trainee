from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(5)  # Simulate a delay
    print("Signal handler finished")

# Simulate a User save operation
user = User(username="john_doe")
user.save()
print("User save operation finished")
