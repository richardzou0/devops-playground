import os
import sys
import subprocess
# File I/O
quote = input("What is your favorite quote?\n")
with open('quote.txt', 'w') as file:
    file.write(quote)
with open('quote.txt', 'r') as file:
    line = file.read()
    print(f'Your saved quote: "{line}"')

# OS Module
print(f"Current directory: {os.getcwd()}")  # Get current working directory
for item in os.listdir():
    print(f"Found file: {item}")  # List files in current directory

# Error Handling
try:
  with open ('notes.txt', 'r') as file:
    contents = file.read()
    print(f"Contents of notes.txt:\n{contents}")
except:
  print("File not found. Please create it first.")

# SYS Module
name = sys.argv[1]
print(f"Hello {name}")
# Run python3 sys_args.py World to see "Hello World"

# Subprocess Module
subprocess.run(["ls", "-l"])