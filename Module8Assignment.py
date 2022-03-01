import os

# Get necessary input
directory = input("Specify a directory: ")
filename = input("Specify a filename: ")
name = input("Name: ")
addr = input("Address: ")
phone = input("Phone: ")

# Make a CSV line
line = f"{name},{addr},{phone}"

# If the directory doesn't exist, create it
if (os.path.isdir(directory) == False):
    os.mkdir(directory)

# Create a complete file path from the directory and filename
filePath = os.path.join(directory, filename)

# Open the file and write the CSV line to it, and close the file
with open(filePath, "a") as fh:
    fh.write(f"{line}\n")
# I'll leave the last part for you to put together (reading the line from the file)
def readFile(filename):
  with open(filename, "r") as fh:
    print("")
    print("-"*6+"File Contents"+"-"*6)
    print(fh.read())
