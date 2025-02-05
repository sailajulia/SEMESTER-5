import imageio as image
import numpy as np
import matplotlib.pyplot as plt

def histEqual(image):
    hist, bins = np.histogram(image.flatten(),bins=256,range=[0,256])
    cdf = hist.sum()
    cdf_normal = (cdf/cdf.max()) * 255
    img_equal = np.interp(image.flatten(),bins [:-1],cdf_normal)
    return img_equal.reshape(image.shape).astype(np.uint8)

image = image.imread ("D:\\Mata Kuliah Semester 5\\Pengolahan Citra Digital\\image\\positif.jpg")
imgEqual = histEqual(image)

plt.figure(figsize=(10,10))

plt.subplot(2,2,1)
plt.imshow(image)

plt.subplot(2,2,2)
plt.imshow(imgEqual)
plt.show()