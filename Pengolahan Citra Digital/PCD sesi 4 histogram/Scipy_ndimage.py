import imageio.v2 as imageio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

image = imageio.imread("D:\\Mata Kuliah Semester 5\\Pengolahan Citra Digital\\image\\positif.jpg", mode="L")

smoothed_image = gaussian_filter(image, sigma=2)

def histogram_equalization(img):
    hist, bin_edges = np.histogram(img.flatten(), bins=256, range=(0, 255))
    cdf = hist.cumsum()
    cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
    cdf_normalized = cdf_normalized.astype('uint8')
    img_equalized = cdf_normalized[img.astype('uint8')]
    return img_equalized

equalized_image = histogram_equalization(image)

plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
plt.title("Citra Asli")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Citra Setelah Gaussian Filter")
plt.imshow(smoothed_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Citra Setelah Ekualisasi Histogram")
plt.imshow(equalized_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
