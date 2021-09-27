# TASK 1
import os


# Complete the function to return the current working directory
def getCurrentDirectory():
    return os.getcwd()


# expected output: /tmp
# if using PyFiddle.io otherwise it varies
print(getCurrentDirectory())

# TASK 2
import os


# Complete the function to return the directory name only from the given file name
def getDirectoryName(fileName):
    return os.path.dirname(fileName)


# expected output: /var/www
print(getDirectoryName("/var/www/test.html"))

# expected output: /var/www/apple
print(getDirectoryName("/var/www/apple/test.html"))

# TASK 3
import os


# Complete the function to return the file name part only from the given file name
def getFileName(fileName):
    return os.path.basename(fileName)


# expected output: test.html
print(getFileName("/var/www/test.html"))

# expected output: names.txt
print(getFileName("/var/www/apple/names.txt"))

# TASK 4
import os


# Complete the function to create the specified file and return the file name
def createFile(filename):
    with open(filename, 'w') as file:
        return file


# expected output: True
createFile("test.txt")
print(os.path.exists("test.txt"))

# TASK 5
import os


# Complete the function to print all files in the given directory
def printFiles(someDirectory):
    print(os.listdir(someDirectory))


# expected output: main.py
# if using PyFiddle.io otherwise it varies
printFiles(os.getcwd())

# TASK 6
import os


# Complete the function to return FILE if the given path is a file
# or return DIRECTORY if the given path is a directory
# or return NEITHER is it's not a file or directory
def whatIsIt(somePath):
    if os.path.isfile(somePath):
        return 'FILE'
    elif os.path.isdir(somePath):
        return 'DIRECTORY'
    else:
        return 'NEITHER'


# expected output: DIRECTORY
print(whatIsIt(os.getcwd()))

# expected output: FILE
print(whatIsIt(os.listdir(os.getcwd())[0]))
# The file in position 0 in my working directory is '.git', which os.path.isfile() doesn't seem to recognize as a file.
# os.path.isdir() instead recognized it as a directory. Is there a way around this?
# I changed the index here to 5 (a .py file) and the function correctly returned 'FILE'.

# expected output: NEITHER
print(whatIsIt('apple.pie.123.txt'))

# TASK 7
import os


# Complete the function to read the contents of the specified file and print the contents
def printFileContents(filename):
    with open(filename, 'r') as f:
        print(f.read())


# expected output: Hello
with open("test.txt", 'w') as f:
    f.write("Hello")
printFileContents("test.txt")

# TASK 8
import os


# Complete the function to append the given new data to the specified file then print the contents of the file
def appendAndPrint(filename, newData):
    with open(filename, 'a') as f:
        f.write(newData)
    with open(filename, 'r') as f:
        print(f.read())


# expected output: Hello World
with open("test.txt", 'w') as f:
    f.write("Hello ")
appendAndPrint("test.txt", "World")
