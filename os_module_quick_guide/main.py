#  get os name
import os
import secrets
from collections.abc import MutableMapping

print(os.name)

# # username of the current user
print(os.getlogin())

# # system information
print(os.uname())

# # get cpu count
print(os.cpu_count())

# #  get random bytes
print(os.urandom(16))


# """
#     using  secrets module to get random bytes and strings
# """
# #  to get random bytes
random_bytes = secrets.token_bytes(16)
print(random_bytes)
# #  to get a URL-safe text string
token_url_safe = secrets.token_urlsafe(16)
print(token_url_safe)

# #  to get a hexadecimal string
token_hex = secrets.token_hex(16)
print(token_hex)


# #  enivronment variables
print(os.environ)

# """

#     os.environ behaves like a dictionary ie it is a MutableMapping

#     Use os.getenv() for reading.

#     Use os.environ[...] for setting.

#     Use os.environ.get() only if you need to interact with the os.environ dict.

# """
print(isinstance(os.environ, MutableMapping))  # True
print(os.environ.get("HOME"))  # get specific env variable

os.putenv("MY_VAR", "my_value")  # set env variable
print(os.getenv("MY_VAR"))  # verify it is set

# # THIS WORKS FOR SETTING ENV VARIABLES
os.environ["ANOTHER_VAR"] = "another_value"  # another way to set env variable
print(os.environ["ANOTHER_VAR"])  # verify it is set
# # Note: Changes made using os.putenv() or os.environ[...] affect only the current process and its children.
# # They do not modify the system-wide environment variables.


#  running system commands
res = os.system('open -a "Activity Monitor"')

print(res)  # 0 if success else error codes
