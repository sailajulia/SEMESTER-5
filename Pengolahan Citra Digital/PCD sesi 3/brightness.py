import  imageio as image
import numpy as np
import matplotlib.pyplot as plt

def brightness(image,factor):
    img_bright = image.astype(np.float32)
    img_bright += factor 
    img_bright = np.clip(img_bright,0,255)
    return img_bright.astype(np.uint8)

def contrast(image, factor):
    imgContrast = image.astype(np.float32)
    mean = 128
    imgContrast = mean + factor * (imgContrast - mean)
    ImgContrast = np.clip(imgContrast,0,255)
    return imgContrast.astype(np.uint8)

def join(image1, f1, image2, f2):
    img1 = image1.astype(np.float32)
    img2 =image2.astype(np.float32)
    imageBlend = (img1 * f1) + (img2 * f2)
    imageBlend = np.clip(imageBlend,0,255)
    return imageBlend.astype(np.uint8)


img = image.imread("D:\\Mata Kuliah Semester 5\\Pengolahan Citra Digital\\image\\positif.jpg")
hist,bins =np.histogram(img.flatten(),bins=256, range=[0,256])

img_contrast = contrast(img,2)
hist_c,bins = np.histogram(img_contrast.flatten(), bins=256, range=[0,256])

img1 = image.imread("C:\\Users\\saila\\Downloads\\Abecekut.jpg")
img2 = image.imread("C:\\Users\\saila\\Downloads\\Abelagi.jpg")

imgBlend = join(img1,0.2,img2,0.8)

plt.figure(figsize=(10,10))

plt.subplot(3,2,1)
plt.imshow(img)

plt.subplot(3,2,2)
plt.imshow(img_contrast)

plt.subplot(3,2,3)
plt.plot(hist)

plt.subplot(3,2,4)
plt.plot(hist_c)

plt.subplot(3,2,5)
plt.imshow(imgBlend)
plt.show()