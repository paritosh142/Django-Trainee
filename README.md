# Solutions to Django and Python Tasks

This repository contains solutions to the questions related to Django Signals and Python custom classes as required for the Django Trainee role at AccuKnox.

---

## 1. Django Signals

### Question 1: By default, are Django signals executed synchronously or asynchronously?
**Answer**: By default, Django signals are executed synchronously. This means that the signal is triggered and executed before the next line of code in the caller function is run.

- [Solution for Question 1: Synchronous or Asynchronous](Solutions/question1_django_signal_sync_async.py)

### Question 2: Do Django signals run in the same thread as the caller?
**Answer**: Yes, Django signals run in the same thread as the caller by default. This can be verified by comparing thread IDs between the signal and the caller.

- [Solution for Question 2: Same Thread](Solutions/question2_django_signal_thread.py)

### Question 3: By default, do Django signals run in the same database transaction as the caller?
**Answer**: Yes, Django signals run in the same database transaction as the caller by default. This means if the caller's transaction fails, the actions taken by the signal handlers will also be rolled back.

- [Solution for Question 3: Same Database Transaction](Solutions/question3_django_signal_transaction.py)

---

## 2. Custom Python Classes

### Task: Create a Rectangle class with the following requirements:
1. An instance of the Rectangle class requires `length: int` and `width: int` to be initialized.
2. We can iterate over an instance of the Rectangle class.
3. When an instance of the Rectangle class is iterated over, we first get its length in the format: `{'length': <VALUE_OF_LENGTH>}` followed by its width `{'width': <VALUE_OF_WIDTH>}`.

- [Solution for Rectangle Class](rectangle_class.py)

---

### How to Run the Code
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
