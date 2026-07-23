import dicom2jpg
import numpy as np

import cv2
import dicom2jpg


def pixel_to_bool(img, x,y):
    return 1 if img[x][y] else 0

def dicom_to_image (dicom_path) :
    image = dicom2jpg.dicom2img(dicom_path)

    success = cv2.imwrite("output.jpg", image)

    if not success:
        raise OSError("OpenCV could not write output.jpg")
    
    return image


def main():
    dicom_path = "ct-lung-screening-nlst-instance.dcm"

    image = dicom_to_image(dicom_path)

    print(type(image))
    print(image.shape)
    print(image.dtype)

    for y in range(image.shape[1]) :
        for x in range(image.shape[0]) :
            print(pixel_to_bool(image, x,y), end = ", ")
        print("\n")
    

if __name__ == "__main__":
    main()