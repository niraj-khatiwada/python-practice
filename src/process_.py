import os
import signal

print("Main ", os.getpid())

os.kill(os.getpid(), signal.SIGTERM)

print("this wont execute")
