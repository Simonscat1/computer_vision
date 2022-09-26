import numpy as np
import matplotlib.pyplot as plt

def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

def result(size):
    image = np.zeros((size*2, size*2, 3), dtype="uint8")
    color1 = [255, 128, 0]
    color2 = [0, 128, 255]
    image = gradient(image, color1, color2)
    image = array(image, size)
    plt.imshow(image)
    plt.show()

def array(image, size):
    image2 = np.zeros((size, size, 3), dtype="uint8")
    for i in range(len(image)):
        for j in range(len(image[i])):
            if(j+size<len(image) and i+size<len(image)):
                image2[i][j]=image[i][j+i]
    return image2

def gradient(image, color1, color2):
    for i, v in enumerate(np.linspace(0, 1, image.shape[0])):
        r = lerp(color1[0], color2[0], v)
        g = lerp(color1[1], color2[1], v)
        b = lerp(color1[2], color2[2], v)
        image[i, :, :]= [r, g, b]
    return np.rot90(image, -1)

result(size=100)