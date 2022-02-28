import os

print(
    'Hi, I can save a new file with your name, address, and phone number, in a specified directory for you, if it is new we will make the directory.')

path = input('Please provide directory name: ')
print(f'The directory name is: {name}')
directoryName = new directoryName

fileName = input('What is the new file name?\n)')
print(f'The file name is:')
filePath = os.path.join('userPath, newFile')
with open(filepath, 'w+') as fp:

name = input("What is your name?\n)")
address = input('What is your address?\n)')
number = input('What is your phone number?\n')
##Create new file
try:
    with open(filePath, 'w') as file_object:
        data = (name + "," + address + "," + number)
        file_object.write(data)
except:
    print('Error creating/writing to new file.')
    quit()
try:
    with open(filePath) as file_object:
        print('New file created,' + 'newFile' + ', and added the following information:')
        print(file_object.read())

def get_name():
  print = ('What is your name?: ')
  userName = input('My name is:')
  print('Hello', name)

print(f'What is your address? ')
address = input('Your address is: ')
print(f'What is your phone number? ')
phoneNum = input('Your phone number is: ')
print(f'{name}, {add}, {phone}')

filePath = os.path.join(directory, filename)

print(f'If it is new enter the name of the new directory')
input('Name the new directory: ')
print(f' {new}')
##Naming the File for the Directory
file = input("The name of the file for the directory: ")
print(f'{file}')
except:
print(('Error reading file.'))

main()