import dicom2jpg
import numpy as np

import cv2
import dicom2jpg


def pixel_to_bool(img, x,y):
    return True if img[x][y] else False

def main():
    dicom_path = "ct-lung-screening-nlst-instance.dcm"

    image = dicom2jpg.dicom2img(dicom_path)

    print(type(image))
    print(image.shape)
    print(image.dtype)

    success = cv2.imwrite("output.jpg", image)

    if not success:
        raise OSError("OpenCV could not write output.jpg")


if __name__ == "__main__":
    main()