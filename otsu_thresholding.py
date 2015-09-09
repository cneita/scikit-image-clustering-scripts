#!/usr/bin/env python
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.filters import threshold_otsu

# 1 x 2 grid figure
fig = plt.figure()

# display original image's channel
cell1 = fig.add_subplot(1, 2, 1)
img = io.imread('flood.jpg')[:, :, 0]
io.imshow(img)

# otsu thresholding of the image
cell2 = fig.add_subplot(1, 2, 2)
threshold = threshold_otsu(img)
thresholded_img = img > threshold
print 'Threshold:', threshold
io.imshow(thresholded_img)

# show figure grid
plt.show()
