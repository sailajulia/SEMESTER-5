import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def zoomMinus(image, factor):
    height, width = image.shape[:2]
    new_height = int(height / factor)
    new_width = int(width / factor)
    imgZoom = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):
            ori_y = int(y * factor)
            ori_x = int(x * factor)

            imgZoom[y, x] = image[ori_y, ori_x]

    return imgZoom

image = img.imread("D:\\Mata Kuliah Semester 5\\Pengolahan Citra Digital\\image\\Abecekut.png")
skala = 2.0  

imgZoom = zoomMinus(image, skala)

img.imwrite("D:\\Mata Kuliah Semester 5\\Hasil_pcd_abe_zoom_minus.png", imgZoom)

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(imgZoom)
plt.title("Zoomed Out Image")

plt.show()
