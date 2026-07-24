import os
import dicom2jpg

folder_path = "./lung-cancer-full-series"

def list_files_in_folder(folder_path) :

    dicom_files = []

    for item in os.scandir(folder_path) :
        if item.is_file() :

            root, extension = os.path.splitext(item)
            if extension == ".dcm" :
                file_name = root + extension
                print("found: " + file_name)
                dicom_files.append(file_name)
    
    return dicom_files

def dicom_to_image(dicom_paths) :

    images = []

    for item in dicom_paths :
        images.append(dicom2jpg.dicom2img(item))
        print("processed: " + item)

    return images


series_files = list_files_in_folder(folder_path)

series_images = dicom_to_image(series_files)