import os

path = input("directory path: ")

if os.path.exists(path):
    items = os.listdir(path)
    
    directories = [item for item in items if os.path.isdir(os.path.join(path, item))]
    print("Directories:")
    if directories:
        print("\n".join(directories))
    else:
        print("No directories found.")
    
    files = [item for item in items if os.path.isfile(os.path.join(path, item))]
    print("\nFiles:")
    if files:
        print("\n".join(files))
    else:
        print("No files found.")
    
    print("\nAll items:")
    print("\n".join(items))
else:
    print("The specified path does not exist!")
