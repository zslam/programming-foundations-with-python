import os

def rename_files():
    #1 get file names from a folder
    file_list = os.listdir("/home/eslam/Programming/Python/Udacity-Foundation with python/secret message puzzle")
    #print(file_list)
    saved_path = os.getcwd()
    os.chdir("/home/eslam/Programming/Python/Udacity-Foundation with python/secret message puzzle")

    #2 for each file, rename file name
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()
