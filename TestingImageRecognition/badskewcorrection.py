# SKEW ADJUSTMENT - THIS IS A LOT OF NEW CODE
# imports
from PIL import Image as im
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import interpolation as inter

filename = 'img/input/image11.jpeg'

# open with PIL
img2 = im.open(filename)

# converting to binary
wd, ht = img2.size
pix = np.array(img2.convert('1').getdata(), np.uint8)
bin_img = 1 - (pix.reshape((ht, wd)) / 255.0)
plt.imshow(bin_img, cmap='gray')
plt.savefig('img/aThresbSkew/binary.png')


# finding the score of the image
def find_score(arr, i_angle):
    i_data = inter.rotate(arr, i_angle, reshape=False, order=0)
    i_hist = np.sum(i_data, axis=1)
    i_score = np.sum((i_hist[1:] - i_hist[:-1]) ** 2)
    return i_hist, i_score


# mathematical skew calculations
delta = 1
limit = 5
angles = np.arange(-limit, limit+delta, delta)
scores = []
for angle in angles:
    hist, score = find_score(bin_img, angle)
    scores.append(score)

# finding the best angle to which we need to correct the skew
best_score = max(scores)
best_angle = angles[scores.index(best_score)]
print('Best angle: {}'.format(best_angle))

# Actually correcting the skew
data = inter.rotate(bin_img, best_angle, reshape=False, order=0)

img2.show()

img2 = im.fromarray((255 * data).astype("uint8")).convert()    # note the comment here
img2.save('img/aThresbSkew/middle.jpeg')

img2.show()
