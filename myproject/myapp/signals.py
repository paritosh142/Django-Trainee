from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
import time

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal started for user: {instance.username}")
    time.sleep(3)  # Simulate a time-consuming process
    print(f"Signal finished for user: {instance.username}")
