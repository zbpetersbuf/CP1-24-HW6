"""
this is mine
pylint
pytest
numpy
pandas
matplotlib
pillow
"""
import os

import pandas as pd

import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image


image_path = '/workspaces/CP1-24-HW6/img.png'
image = Image.open(image_path).convert('L')

width, height = image.size
min_dim = min(width, height)

left = (width - min_dim) // 2
top = (height - min_dim) // 2
right = (width + min_dim) // 2
bottom = (height + min_dim) // 2

image_cropped = image.crop((left, top, right, bottom))

image_array = np.array(image_cropped)
FS = np.fft.fft2(image_array)

Y, X = np.meshgrid(np.fft.fftfreq(min_dim), np.fft.fftfreq(min_dim))
FS_filtered = FS * (np.sqrt(X**2 + Y**2) < 0.1)
image_filtered = np.fft.ifft2(FS_filtered)


plt.figure(figsize=(12, 6))
plt.subplot(1, 5, 1)
plt.imshow(image_array)
plt.subplot(1, 5, 2)
plt.imshow(np.log(np.abs(FS) + 1))
plt.subplot(1, 5, 3)
plt.imshow(np.real(np.fft.ifft2(FS)))
plt.subplot(1, 5, 4)
plt.imshow(np.log(np.abs(FS_filtered) + 1))
plt.subplot(1, 5, 5)
plt.imshow(np.real(image_filtered))



plt.tight_layout()
plt.show()

plt.show()

plot = input("Do you want to save the plot? (yes/no): ").strip().lower()

if plot == 'yes':
    fpath = input("enter where to save: ").strip()
    if not os.path.exists(fpath):
        print("Directory does not exist, try again")
    else:
        filpath = os.path.join(fpath, "workin it.png")
        plt.savefig(filpath, format='png', dpi=400)
        print(f"Plot saved as {filpath}")
else:
    print("Plot not saved.")