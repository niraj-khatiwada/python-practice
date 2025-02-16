import time
import random
from threading import Thread

balance = 100


def withdraw(amount):
    global balance
    if amount > balance:
        raise Exception("Not enough balance.")
    time.sleep(random.randint(1, 5))
    balance -= amount
    print(f"Withdraw of {amount} successful. Remaining balance = {balance}.")


thread1 = Thread(target=withdraw, args=(90,))
thread2 = Thread(target=withdraw, args=(20,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# Output
# Withdraw of 20 successful. Remaining balance = 80.
# Withdraw of 90 successful. Remaining balance = -10.

# Race condition occurred here
