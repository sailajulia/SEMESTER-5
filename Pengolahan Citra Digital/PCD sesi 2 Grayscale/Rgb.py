import numpy as np
import imageio.v3 as img

def process_image(image_path, output_prefix, color):
    image = img.imread(image_path)

    if len(image.shape) < 3 or image.shape[2] != 3:
        print(f"Format gambar harus RGB: {image_path}")
        return

    red = image[:, :, 0]
    green = image[:, :, 1]
    blue = image[:, :, 2]

    image_color = np.zeros_like(image)

    if color == "red":
        image_color[:, :, 0] = red  
    elif color == "green":
        image_color[:, :, 1] = green  
    elif color == "blue":
        image_color[:, :, 2] = blue  
    elif color == "grayscale":
        gray = 0.299 * red + 0.587 * green + 0.144 * blue
        image_color[:, :, 0] = gray
        image_color[:, :, 1] = gray
        image_color[:, :, 2] = gray
    elif color == "binary":
        gray = 0.299 * red + 0.587 * green + 0.144 * blue
        threshold = 100
        binary_image = np.where(gray > threshold, 255, 0).astype(np.uint8)
        image_color[:, :, 0] = binary_image  
        image_color[:, :, 1] = binary_image  
        image_color[:, :, 2] = binary_image  
    
    img.imwrite(f"{output_prefix}_{color}.jpg", image_color)
    print(f"Proses Berhasil untuk gambar: {image_path} dengan warna {color}")

image_paths = [
    "D:\\Mata Kuliah Semester 5\\Pengolahan Citra Digital\\Daun pepaya.jpeg",
    "D:\\Mata Kuliah Semester 5\\Pengolahan Citra Digital\\Kenikir.jpeg",
    "D:\\Mata Kuliah Semester 5\\Pengolahan Citra Digital\\Singkong.jpeg"
]

output_prefixes = ["Daun_pepaya", "Kenikir", "Singkong"]

colors = ["grayscale"]

for image_path, output_prefix in zip(image_paths, output_prefixes):
    for color in colors:
        process_image(image_path, output_prefix, color)
