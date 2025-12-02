"""
Demonstrating os.popen to run a system command and capture its output
better than running os.system as it allows us to capture output

"""

import os

""" os.popen will allow us to take input or get output """
process = os.popen("ls -lah")
pwd = process.readlines()
process.close()


for line in pwd:
    print(line.strip())


process = os.popen("wc", "w", buffering=1024)
process.write("Hello World\n This is a test.\n")
process.close()
