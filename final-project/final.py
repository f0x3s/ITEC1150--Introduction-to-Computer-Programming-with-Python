import dicom2jpg
import numpy as np
import math
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

def box_blur(image, recurse_level, box_radius=1):

    height = image.shape[0]
    width = image.shape[1]

    horizontal = image.astype(float)
    blur = image.copy()

    print(box_radius)
    for y, row in enumerate(image) :
        for x, pixel in enumerate(row) :
            pixel_sum = 0
            count = 0

            for offset_x in range(-box_radius, box_radius) :
                local_x = x + offset_x

                if local_x >= 0 and local_x < width :
                    pixel_sum += int(image[y][local_x])
                    count += 1
            
            horizontal[y][x] = pixel_sum/count

    for y, row in enumerate(horizontal) :
        for x, pixel in enumerate(row) :
            pixel_sum = 0
            count = 0

            for offset_y in range(-box_radius, box_radius) :
                local_y = y + offset_y

                if local_y >= 0 and local_y < height :
                    pixel_sum += int(horizontal[local_y][x])
                    count += 1
            
            blur[y][x] = round(pixel_sum/count)

    if recurse_level > 1 :
        return box_blur(blur, recurse_level - 1, box_radius + 1)
    else :
        return blur



def main():
    dicom_path = "ct-lung-screening-nlst-instance.dcm"

    image = dicom_to_image(dicom_path)

    print(type(image))
    print(image.shape)
    print(image.dtype) 

   
    image = box_blur(image,4)

    layers = []

    for layer in range(63) :
        layers.append(thresh_image(image,((256/63) * layer)))
        print("=", end="")

    i = 0
    while True :
        cv2.imshow('Image Window', layers[i])
        cv2.waitKey()
        i += 1

        if i == len(layers) :
            i = 0


if __name__ == "__main__":
    main()