import numpy as np
from scipy import ndimage

def mask():
     masks = np.array([
          np.array([
               [1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 0, 0],
               [1, 1, 0, 0],
               [1, 1, 1, 1],
               [1, 1, 1, 1]
          ]), 
          np.array([
               [1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1],
               [1, 1, 0, 0, 1, 1],
               [1, 1, 0, 0, 1, 1]
          ]),    
          np.array([
               [1, 1, 0, 0, 1, 1],
               [1, 1, 0, 0, 1, 1],
               [1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1]
          ]), 
          np.array([[1, 1, 1, 1],
                    [1, 1, 1, 1],
                    [0, 0, 1, 1],
                    [0, 0, 1, 1],
                    [1, 1, 1, 1],
                    [1, 1, 1, 1]
          ]),
          np.array([[1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1]
          ])], dtype=object)
     return masks

def bi_hist(masks, image):
     result = 0
     i = 0
     for mask in masks:
          r = ndimage.binary_hit_or_miss(image, mask)
          i += 1
          print(f"Количество фигур под номером - {i}, равно: {np.sum(r)}")
          result += np.sum(r)
     return result
     
image = np.load('ps.npy')
result = bi_hist(mask(), image)

print(f'Общее количество фигур равно: {result}')