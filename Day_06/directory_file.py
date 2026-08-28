#Get Current Directory in Python
import os
print("Current Directory:", os.getcwd())

#Changing Directory in Python
#change directory
os.chdir("C:\\Users\\ali.imtiaz\\Desktop")
print("Current Directory:", os.getcwd())

#List Directories and Files in Python
import os

print("Current Directory:", os.getcwd())
# Example output: C:\Python33

# list all sub-directories
print(os.listdir())
# Example output:
# ['DLLs',
# 'Doc',
# 'include',
# 'Lib',
# 'libs',
# 'LICENSE.txt',
# 'NEWS.txt',
# 'python.exe',
# 'pythonw.exe',
# 'README.txt',
# 'Scripts',
# 'tcl',
# 'Tools']

print(os.listdir('G:\\'))
# Example output:
# ['$RECYCLE.BIN',
# 'Movies',
# 'Music',
# 'Photos',
# 'Series',
# 'System Volume Information']


#Making a New Directory in Python
os.mkdir("C:\\Users\\ali.imtiaz\\Desktop\\New Folder")
os.listdir("C:\\Users\\ali.imtiaz\\Desktop")
['New Folder', 'Python', 'Python 3.11.4', 'Python 3.11.4 (64-bit)', 'Python 3.11.4 (64-bit) - Shortcut', 'Python 3.11.4 - Shortcut', 'Python 3.11.4 - Shortcut.lnk', 'Python 3.11.4.lnk', 'Python 3.11.4.lnk.lnk', 'Python 3.11.4.lnk.lnk.lnk', 'Python 3.11.4.lnk.lnk.lnk.lnk', 'Python 3.11.4.lnk.lnk.lnk.lnk.lnk', 'Python 3.11.4.lnk.lnk.lnk.lnk.lnk.lnk', 'Python 3.11.4.lnk.lnk.lnk.lnk.lnk.lnk.lnk', 'Python 3.11.4.lnk.lnk.lnk.lnk.lnk.lnk.lnk.lnk', 'Python 3.11.4.lnk.lnk.lnk.lnk.lnk.lnk.lnk.lnk.lnk', 'Python 3.11.4.lnk.lnk.lnk.lnk.lnk.lnk.lnk.lnk.lnk', 'Python 3.11.4.lnk.lnk.lnk.lnk.lnk.lnk.lnk.lnk.lnk.lnk', 'Python 3.11.4.lnk.lnk.lnk.lnk']


#Renaming a Directory or a File

import os

os.listdir()
['test']

# rename a directory
os.rename('test','new_one')

os.listdir()
['new_one']

#Removing Directory or File in Python
import os

# delete "myfile.txt" file
os.remove("myfile.txt")