# Accept file name from user
filename = input("Enter the file name: ")

# Find position of last dot
pos = filename.rfind(".")

# Print extension if dot found
if pos != -1:
    print("The file extension is:", filename[pos+1:])
else:
    print("No extension found.")
