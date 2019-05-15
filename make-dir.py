"""
@author: Ramkishan K Pawar
Python script to create empty directory.
"""
import os

directory = input("Enter the name of the directory: ")

try:
    folder = os.mkdir(directory)
    print("Directory created successfully !")
except(FileExistsError):
    print("Directory Already Exists !")
