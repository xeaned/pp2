import os

path = input("enter the path: ")

if os.path.exists(path):
    print("path exists")
    
    directory = os.path.dirname(path)
    print(f"directory: {directory}")
    
    filename = os.path.basename(path)
    print(f"filename: {filename}")
else:
    print("the path does not exist")