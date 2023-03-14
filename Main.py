import os
source= "main.txt"
dest="newfile.txt"

for file in os.listdir(source):
    name, ext = os.path.splitext(file)

os.rename(source,dest)
print("Source Path Renamed to Destination Path Successfully")