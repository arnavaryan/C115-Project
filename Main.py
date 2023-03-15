import os 
source="C:/Users/malho_9yypg6y/Desktop/Coding/C115 Project/main.txt" 
name=os.path.splitext(source) 
os.rename(source,"newfile.txt") 
print("Source Path Rename to Destination Path Successfully")
