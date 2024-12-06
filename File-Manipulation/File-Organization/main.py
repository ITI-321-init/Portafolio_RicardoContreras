"""================================================================================================
University...: Universidad Técnica Nacional
Campus.......: Pacífico
Career.......: Tecnologías de la Información
Course.......: ITI-321 - Programación II
Period.......: 3-2024
Document.....: File-Organization/main.py
Goals........: file handling: navigate, rename, move, copy, remove
Professor....: Jorge Ruiz (york)
Student......: Ricardo Contreras
================================================================================================"""
#file handling: navigate, rename, move, copy, remove
import os
import shutil
from contextlib import chdir
from pathlib import Path
#---------------------------------(Printing extension & Files names)---------------------------------




print('---------------------------------(Printing extension & Files names)---------------------------------')
print(os.getcwd())

os.chdir('/home/tenshi/Desktop/File_manipulation/File_Manipulation/assets')

print(os.getcwd())

print(os.listdir())
print('---------------------------------------')
#Iteration print method:
for file in os.listdir():
    print(file)
print('---------------------------------------')
print('-----(printing file and extension separated)-----')
for file in os.listdir():
    name , ext = os.path.splitext(file)
    print(name)
    print(ext)
print('---------------------------------------')



#---------------------------------(Changing files name and navigating)---------------------------------

print('---------------------------------(Changing files name and navigating)---------------------------------')

#NOTICE THIS: Python will NOT return to the origin directory, if you move.txt ones, it will stay there, YOU NEED TO GO BACK
main_directory = ('/home/tenshi/Desktop/File_manipulation/File_Manipulation/File-Organization')
#print(main_directory)
#print(os.listdir(main_directory))
assets_directory = ('/home/tenshi/Desktop/File_manipulation/File_Manipulation/assets')
#print(assets_directory)
#print(os.listdir(assets_directory))


#NOTICE: I'm on Assets
os.chdir(assets_directory)
#print(os.getcwd())

file_name = input('Enter file name INCLUDING the extension: ')



"""if os.path.exists(assets_directory):
    new_file_name = input('Enter new file name INCLUDING the extension: ')
    os.rename(file_name, new_file_name)
    print(f'old file name is {file_name} and new file name is {new_file_name}')
else:
    print('No file found on Assets Directory')"""



try:
    if os.path.exists(assets_directory):
        new_file_name = input('Enter new file name INCLUDING the extension: ')
        os.rename(file_name, new_file_name)
        print(f'old file name is {file_name} and new file name is {new_file_name}')
    else:
        print('No file found on Assets Directory')
except:
    print('Error, file not found or name was not change')

#NOTICE: back in main
os.chdir(main_directory)
#print(os.getcwd())

#---------------------------------(Moving files)---------------------------------

print('---------------------------------(Moving files)---------------------------------')
#NOTICE: I'm on Assets
os.chdir(assets_directory)

#N0TICE: this will create a new directory on assets call Move_Directory, this new directory will exist temporally

if not os.path.exists('Move_Directory'):
    print('Move Directory does not exist')
    print('Moving move.txt to Move_Directory')
    os.mkdir('Move_Directory')
    shutil.move('move.txt', 'Move_Directory')

else:
    print('Move directory already exists')
    print('Moving back move.txt file to Directory root')
    shutil.rmtree('Move_Directory')
    assets_directory = os.path.join(assets_directory, 'move.txt')
    with open(assets_directory, 'w') as move:
        move.write('this file will move DO NOT REMOVE')

#NOTICE: back in main
os.chdir(main_directory)

#---------------------------------(#Copying files)---------------------------------

print('---------------------------------(Copying files)---------------------------------')
copy_Destination = '/home/tenshi/Desktop/File_manipulation/File_Manipulation/assets/Copy_Directory'
#NOTICE: I'm on Copy Directory
os.chdir(copy_Destination)

try:
    if os.path.exists('file_copy.txt'):
        os.remove('file_copy.txt')
        print('file_copy removed')
    else:
        print ('file_copy does not exist, creating file')
        # NOTICE: I'm on Assets
        os.chdir(assets_directory)

        shutil.copy('file_copy.txt', 'Copy_Directory')
except Exception as e:
    print('Error on file_copy.txt deletion if')

#NOTICE: back in main
os.chdir(main_directory)






















