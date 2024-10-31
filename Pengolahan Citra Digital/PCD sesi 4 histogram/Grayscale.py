import imageio.v2 as image
import numpy as np
import matplotlib.pyplot as plt

path = "D:\\Mata Kuliah Semester 5\\Pengolahan Citra Digital\\Abe.jpeg"

my_image = image.imread(path)

if len(my_image.shape) < 3:
    print("Gambar input harus RGB")
    exit()

red = my_image[:, :, 0]
green = my_image[:, :, 1]
blue = my_image[:, :, 2]

gray = (red + green + blue) / 3

image_red = np.zeros_like(my_image)
image_red[:, :, 0] = red

image_green = np.zeros_like(my_image)
image_green[:, :, 1] = green

image_blue = np.zeros_like(my_image)
image_blue[:, :, 2] = blue

image_gray = np.zeros_like(my_image)
image_gray[:, :, 0] = gray
image_gray[:, :, 1] = gray
image_gray[:, :, 2] = gray

threshold_bw = 128
image_bw = np.zeros_like(my_image)
image_bw[gray > threshold_bw] = 255
image_bw[gray <= threshold_bw] = 0

image_gray = image_gray.astype("uint8")
image_bw = image_bw.astype("uint8")

image.imwrite("D:\\Mata Kuliah Semester 5\\Pengolahan Citra Digital\\Abe.jpeg", image_red)
image.imwrite("D:\\Mata Kuliah Semester 5\\Pengolahan Citra Digital\\Abe.jpeg", image_green)
image.imwrite("D:\\Mata Kuliah Semester 5\\Pengolahan Citra Digital\\Abe.jpeg", image_blue)
image.imwrite("D:\\Mata Kuliah Semester 5\\Pengolahan Citra Digital\\Abe.jpeg", image_gray)
image.imwrite("D:\\Mata Kuliah Semester 5\\Pengolahan Citra Digital\\Abe.jpeg", image_bw)

print(f"Dimensi Gambar Adalah {my_image.shape}")
print("Proses Selesai!")

def plot_histogram(channel_data, color, title):
    plt.figure(figsize=(10, 6))
    plt.hist(channel_data.ravel(), bins=256, color=color, alpha=0.7)
    plt.title(title)
    plt.xlabel('Intensitas Piksel')
    plt.ylabel('Frekuensi')
    plt.grid(axis='y')
    plt.show()

plot_histogram(red, 'red', 'Histogram Saluran Merah')
plot_histogram(green, 'green', 'Histogram Saluran Hijau')
plot_histogram(blue, 'blue', 'Histogram Saluran Biru')
plot_histogram(gray, 'gray', 'Histogram Gambar Grayscale')