import  imageio as image
import numpy as np
import matplotlib.pyplot as plt

path = "D:\\Mata Kuliah Semester 5\\Pengolahan Citra Digital\\positif.jpg"
img_Negatif = image.imread(path)
r_neg = img_Negatif[:, :, 0]

hist_rneg, bins =np.histogram(r_neg.flatten(), bins=256,range=[0,256])

img_positif = 255 - img_Negatif

plt.figure(figsize=(15, 15))

plt.subplot(4, 1, 1)
plt.imshow(img_Negatif)

plt.subplot(4, 1, 2)
plt.imshow(img_positif)

plt.subplot(4, 1, 3)
plt.plot(hist_rneg)

plt.show()
print(img_Negatif.shape)
