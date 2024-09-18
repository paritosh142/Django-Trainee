# Yes, Django signals run in the same thread as the caller. We can confirm this by checking the thread ID during the signal handling.

# ############################## #

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")

# Simulate a User save operation
print(f"Caller thread ID: {threading.get_ident()}")
user = User(username="jane_doe")
user.save()


# ############################## #

# The output of the code snippet above will be:

# Caller thread ID: 140736043462592
# Signal handler thread ID: 140736043462592

# This confirms that Django signals run in the same thread as the caller. The thread ID remains the same throughout the process