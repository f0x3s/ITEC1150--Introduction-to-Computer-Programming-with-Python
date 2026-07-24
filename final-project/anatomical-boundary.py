import os

folder_path = "./lung-cancer-full-series"

def list_files_in_folder(folder_path) :

    for item in os.scandir(folder_path) :
        if item.is_file() :
            root, extension = os.path.splitext(item)
            if extension == ".dcm" :
                print(root)


list_files_in_folder(folder_path)