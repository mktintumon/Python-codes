import numpy as np
import scipy.io as sio
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Import medical image data into NumPy array
image_np = np.load('medical_image.npy')

# Import medical image data into SciPy array
image_sci = sio.loadmat('medical_image.mat')['data']

# Import medical image data into Pandas DF
image_pd = pd.read_csv('medical_image.csv').values

# Displaying 2D representation of the medical image
plt.imshow(image_np, cmap='gray')
plt.title('2D Representation')
plt.show()


# Displaying 3D representation of the medical image
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
z, y, x = np.nonzero(image_np)
ax.scatter(x, y, -z, c='b', marker='.')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Representation')
plt.show()