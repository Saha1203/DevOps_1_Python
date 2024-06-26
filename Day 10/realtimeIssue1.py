# #list all the files in list of folders that user provides.
# #which file takes maximum size
# import os

# foldersList = input("Please provide list of folders name with spaces in between: ").split()

# for folder in foldersList:


import os

folders = input("Please provide list of folders name with spaces in between: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("***Please provide a valid folder name , looks this folder does not exist: ***"+ folder)
        break
    except PermissionError:
        break
        # print("No access to this folder:")
    print("**** Listing files for the folder -- "+folder)
    # files = os.listdir(folder)
    for file in files:
        print(file)

# foldersList = os.listdir("C:/Users/rahul/OneDrive/Desktop/DevOps/Python/DevOps_1_Python")
# for folder in foldersList:
#     print(folder)