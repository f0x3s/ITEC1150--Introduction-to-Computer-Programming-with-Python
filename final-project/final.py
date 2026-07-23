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

def thresh_image(image, value) :
    thresh = image.copy()

    for y, row in enumerate(thresh) :
        for x, pixel in enumerate(row) :
            thresh[y][x] = 255 if pixel > value else 0

    return thresh

def box_blur(image, level):
    blur = image.copy()

    for y, row in enumerate(image):
        for x, pixel in enumerate(row):
            pixel_sum = 0
            count = 0

            for nbr_y in [-1, 0, 1]:
                for nbr_x in [-1, 0, 1]:
                    local_y = y + nbr_y
                    local_x = x + nbr_x

                    if (0 <= local_y < image.shape[0] and 0 <= local_x < image.shape[1]):
                        pixel_sum += int(image[local_y][local_x])
                        count += 1

            blur[y][x] = round(pixel_sum / count)

    if level > 0 :
        return box_blur(blur, level-1)
    else :
        return blur



def main():
    dicom_path = "ct-lung-screening-nlst-instance.dcm"

    image = dicom_to_image(dicom_path)

    print(type(image))
    print(image.shape)
    print(image.dtype) 

    image = thresh_image(image,127)
    image = box_blur(image,10)

    cv2.imshow('Image Window', image)
    cv2.waitKey()

if __name__ == "__main__":
    main()