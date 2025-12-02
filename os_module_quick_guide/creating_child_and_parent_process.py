import os
import time

print("Starting")
pid = os.fork()

if pid:
    # Parent process
    print(f"Parent waiting 5 seconds for child (pid={pid})")
    time.sleep(5)
    os.kill(pid, 9)
else:
    # Child process
    while True:
        print("Child running...")
        time.sleep(1)

print("Finished")
