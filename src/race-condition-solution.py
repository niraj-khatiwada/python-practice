import time
import random
from threading import Thread, Lock

balance = 100


def withdraw(amount, lock):
    lock.acquire()
    global balance
    if amount > balance:
        raise Exception("Not enough balance.")
    time.sleep(random.randint(1, 3))
    balance -= amount
    lock.release()
    print(f"Withdraw of {amount} successful. Remaining balance = {balance}.")


lock = Lock()  # Mutex lock
thread1 = Thread(
    target=withdraw, args=(90, lock), daemon=True
)  # daemon = Exit when main thread exists
thread2 = Thread(target=withdraw, args=(20, lock), daemon=True)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
