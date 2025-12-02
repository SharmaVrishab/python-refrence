#  to work with files and directories
import pathlib
from pathlib import Path

#  get absolute path
pwd = pathlib.Path.cwd()
print(f"Current working directory: {pwd}")
print(pwd.parts)


#  get relative path
curr = pathlib.Path(".")
#  get absolute path from relative path
print(curr.resolve())

#  checking the path
print(pwd.exists())  # Check if path exists
print(pwd.is_dir())  # Check if path is a directory
print(pwd.is_file())  # Check if path is a file
print(pwd.is_absolute())  # Check if path is absolute
print(pwd.parent)  # Parent directory ie one directory up
"""
pwd.root

root gives the root of the filesystem.

On POSIX (Linux/Mac), this is /.

On Windows, it could be something like C:
"""
print(pwd.root)  # Root of the file system

# "checking which directory is higher in the hierarchy"
up = pwd.parent
print(up < pwd)
print(up > pwd)

#  get the list of files and directories in the current directory
child_files = list(pwd.iterdir())
for child in child_files:
    print(child)


if_files = [pth for pth in pwd.iterdir() if pth.is_file()]
print("Files only:")
for c in if_files:
    print(c)

if_dir = [pth for pth in pwd.iterdir() if pth.is_dir()]
print("Directories only:")
for d in if_dir:
    print(d)


# checking particular files
py_file = list(pwd.glob("*.py"))
print(py_file)


# creatign path for a file inside a sub directory
new_path = pwd.joinpath("subdir", "newfile.txt")
print(new_path)


#  instead of joinpath we can also use the / operator
another_path = pwd / "subdir" / "anotherfile.txt"
print(another_path)
# both new_path and another_path will point to different files inside the subdir directory


curr = pathlib.Path(".") / "subdir" / "file.txt"
print(curr)


print(curr.exists())  # Check if the file exists
print(curr.is_file())  # Check if it's a file
print(curr.name)  # check name of the file
print(curr.suffix)  # check file extension
print(curr.stem)  # check file name without extension


print(curr.with_suffix(".sh"))  # change file extension to .sh

#  this will not create the file evn though the path is for a file
curr.parent.mkdir(
    parents=True, exist_ok=True
)  # create the subdir directory if it doesn't exist
# this will actually create the file for the path
curr.touch(exist_ok=True)  # create the file.txt if it doesn't exist
print(curr.exists())  # now the file should exist


# removing the file
curr.unlink()  # delete the file
print(curr.exists())  # now the file should not exist


#  LAST EXAMPLE

myfile = Path("my_dir_example/example.txt")
print(myfile.resolve())  # Get the absolute path of example.txt
myfile.parent.mkdir(parents=True, exist_ok=True)  # Create parent directories if needed
myfile.touch(exist_ok=True)  # Create the file if it doesn't exist


#  WORKING WITH CONTENT OF FILES

# FOR LARGER FILES
# with myfile.open(mode="w", encoding="utf-8") as f:
#     f.write("Hello, World!\n")
#     f.write("This is a test file.\n")

# FOR SMALLER FILES
#  simpler way to write text to a file
myfile.write_text("Hello, World!\nThis is a test file.\n", encoding="utf-8")
myfile.write_bytes(b"Some binary data.\n")


#  reading the file content
myfile_content = myfile.read_text(encoding="utf-8")
print("File content:")
print(myfile_content)


# cleaning up
myfile.unlink()  # delete the file
myfile.parent.rmdir()  # delete the my_dir_example directory


# working with home

home = Path.home()
print(f"Home directory: {home}")
