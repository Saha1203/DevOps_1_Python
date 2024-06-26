import os

def listFilesInFolder(folderPath):
    try:
        files = os.listdir(folderPath)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permissin denied"
    # return None, "Permission denied"

def main():
    folderPaths = input("Enter a list of folder paths separated by spaces: ").split()

    for folderPath in folderPaths:
        files, errorMessage = listFilesInFolder(folderPath)
        if files:
            print(f"Files in {folderPath}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folderPath}: {errorMessage}")


if __name__ == "__main__":
    main()