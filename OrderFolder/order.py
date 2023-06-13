import os
import shutil

directory = "/Users/marcovinciguerra/Github/Python/OrderFolder" 

dict = {".pdf": "files",
        ".png": "pictures",
        ".mkv": "videos",
        ".doc": "documents",
        ".docx": "documents",
        ".csv": "sheets",
        ".xlsx": "sheets",
        ".xls": "sheets",
        }

listFolders = ["/videos", "/sheets", "/files", "/pictures"]

def createFolders():
    
    for elem in listFolders:
        toAdd = directory+elem
        if not os.path.exists(toAdd):
            os.makedirs(toAdd) 

def getList():
    dir_list = os.listdir(directory)
    print(dir_list)

    return dir_list

def main():
    createFolders()
    
    ListFiles = getList()

    for elem in ListFiles:
        filename, file_extension = os.path.splitext(elem)
        print(elem)
        if(file_extension != "" and file_extension!=".py"):
            print(dict[file_extension])
            shutil.move(directory+"/"+elem, directory+"/"+dict[file_extension]+"/"+elem)

if __name__ == "__main__":
    main()

