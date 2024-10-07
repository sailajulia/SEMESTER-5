import numpy as np
import imageio.v3 as img

image_path = "D:\\Saila\Me\Saila Cantik.jpg"
image = img.imread(image_path)


if len(image.shape) < 3 or image.shape [2] !=3:
    print("format gambar harus RGB")
    exit()
    
red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

image_red = np.zeros_like(image)
image_gray= np.zeros_like(image)

image_red[:,:,0] = red
gray = 0.299 * red + 0.587 * green + 0.144 * blue

image_gray[:,:,0]=gray
image_gray[:,:,1]=gray
image_gray[:,:,2]=gray

img.imwrite("red_image.jpg",image_red)
img.imwrite("gray_image.jpg",image_gray)

print("proses Berhasil")

treshold = 100
binary_image = np.where(gray > treshold, 255, 0).astype(np.uint8)
binary_rgb = np.zeros_like(image)
binary_rgb[:,:,0] = binary_image
binary_rgb[:,:,1] = binary_image
binary_rgb[:,:,2] = binary_image
img.imwrite("image_binary.jpg", binary_rgb)
print("Proses Berhasil")