from matplotlib import pyplot as plt
from skimage.measure import label, regionprops
from skimage import color
import numpy as np

def find_colors(figures):
     colors = {
          "red": 0,
          "orange" : 0, 
          "yellow" : 0, 
          "green" : 0, 
          "light_blue" : 0, 
          "blue" : 0, 
          "purple" : 0
     }
     for i in figures:
          if 15 <= i <= 40:
               colors["orange"] += 1
          if 40 <= i <= 80:
               colors["yellow"] += 1
          if 80 <= i <= 130:
               colors["green"] += 1
          if 130 <= i <= 190:
               colors["light_blue"] += 1
          if 190 <= i <= 260:
               colors["blue"] += 1
          if 260 <= i <= 310:
               colors["purple"] += 1
          if (310 <= i <= 360) or (0 <= i <= 15):
               colors["red"] += 1
     return colors    

def binary_img(image):
     binary = image.copy()[:, :, 0]
     binary[binary > 0] = 1
     labeled = label(binary)
     print(f"All figures: {np.max(labeled)}")

     return labeled

def bals_and_rects(image):
     image_hue = color.rgb2hsv(image)[:, :, 0] * 360
     bals = []
     rect = []
     for region in regionprops(binary_img(image)):
          y, x, y1, x1  = region.bbox
          value = np.max(image_hue[y:y1, x:x1])
          if region.extent == 1:
               rect.append(value)
          else:
               bals.append(value)
     print(f"Count balls: {len(bals)}, colors: {find_colors(bals)}")
     print(f"Count rectangles: {len(rect)}, colors: {find_colors(rect)}")
     return image_hue
image = plt.imread("balls_and_rects.png")
image = bals_and_rects(image)

plt.figure()
plt.imshow(image)
plt.show()