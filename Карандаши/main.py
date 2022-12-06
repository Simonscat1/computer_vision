import numpy as np
from matplotlib import pyplot as plt
from skimage.filters import threshold_otsu
from skimage.measure import regionprops, label

def binory_img(image):
     binory_imeges = []
     for image in image:
          binory_imeges.append(np.mean(image, 2))

     result_images = []
     for image in binory_imeges:
          result_images.append(image < threshold_otsu(image))

     return result_images

def sum_pencils(image):
     pencils_count = list()
     for img in binory_img(image):
          count= 0
          labels = label(img)
          for region in regionprops(labels):
               if (region.perimeter > 2500):
                    if(30 > (region.major_axis_length / region.minor_axis_length) > 15):
                         count += 1
          pencils_count.append(count)
     return np.sum(pencils_count)

image = []
for i in range(1,13):
     image.append(plt.imread(f'./images/img ({i}).jpg'))

print(sum_pencils(image))