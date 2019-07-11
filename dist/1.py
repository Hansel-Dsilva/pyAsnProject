from time import sleep
import sys
print("""1. Write a Python program to get the Python version you are using""")
sleep(1)
print("The current version of this Python Interpreter is " + str(sys.version_info[0]) + "." + str(sys.version_info[1]))