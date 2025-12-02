"""

communicating b/n parent and child process using os.pipe

"""

import os
import time

# Create a pipe
r_desc, w_desc = os.pipe()
p_id = os.fork()

if p_id:
    # Parent
    os.close(r_desc)
    values = ["Process Data 1", "Process Data 2", "Process Data 3"]
    for val in values:
        os.write(w_desc, val.encode() + b"\n")
        print(f"Parent sent: {val}")
        time.sleep(1)
    os.close(w_desc)
    os.wait()
else:
    # Child
    os.close(w_desc)
    with os.fdopen(r_desc) as pipe:
        for line in pipe:
            print(f"Child received: {line.strip()}")
            time.sleep(0.5)
    os._exit(0)
