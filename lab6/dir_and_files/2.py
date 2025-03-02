import os
path = str(input("directory path: "))
print(os.access(path, os.F_OK)) # Existence
print(os.access(path, os.R_OK)) # Read
print(os.access(path, os.W_OK)) # Write
print(os.access(path, os.X_OK)) # Execute