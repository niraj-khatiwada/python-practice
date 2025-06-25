import os
from threading import Thread, current_thread
from multiprocessing import Queue
import time


# Thread: Within a single process, you can run tasks within multiple threads usually to solve blocking issue of one thread. Since, threads live within same process, they can share the memory. So it's easier to pass data between threads unlike processes.
# The API is same as Process()


def factorial(num):
    time.sleep(0.5)
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


threads = []

for i in range(1, os.cpu_count()):
    threads.append(Thread(target=factorial, args=(i,)))

for t in threads:
    t.start()

for t in threads:
    t.join()

# When running this program, you should see only one process being run that is utilizing all `os.cpu_count` number of threads for efficiency
# See threads.png image


# Using Queue to store the result


def worker(num, queue):
    queue.put((current_thread().name, factorial(num)))


queue = Queue()

worker_threads = []

for i in range(1, os.cpu_count()):
    worker_threads.append(Thread(target=worker, args=(i, queue)))

for t in worker_threads:
    t.start()


for t in worker_threads:
    t.join()

while not queue.empty():
    print(queue.get())
