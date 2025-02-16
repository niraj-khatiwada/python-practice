import os
from multiprocessing import process, Process, Pool
import time


# Process: When a program executes it is called a process. Each process has it's own memory and reference id. Since, each process has their own memory, it is difficult to pass data between processes.

# Single process
print(os.getpid())

# For multi process
print(process.current_process().pid)


def factorial(num):
    time.sleep(0.5)
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


processes = map(
    lambda i: Process(target=factorial, kwargs={"num": i}), list(range(os.cpu_count()))
)

for p in processes:
    p.start()
    print("Child process id= ", p.pid)  # Can only access pid after starting the process

for p in processes:
    p.join()

# The downside of using Process() is, we cannot get the return value of factorial here


# SOLUTION: Use Pool instead
def worker(num):
    print("Process id= ", os.getpid())
    return factorial(num)


with Pool(os.cpu_count()) as pool:
    rs = pool.map(
        worker, range(os.cpu_count())
    )  # Pool takes the worker function and optional arguments as iterable
    print("Result from ", rs)

# When you run this file, you should see `os.cpu_count()` number of processes running in your "System Monitor" application.
# See multiprocessing.png image
