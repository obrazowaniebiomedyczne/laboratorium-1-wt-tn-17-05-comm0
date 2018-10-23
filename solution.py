"""
Rozwiązania do laboratorium 1 z Obrazowania Biomedycznego.
"""
import numpy as np

"""
3 - Kwadrat
"""
def square(size, side, start):
    image = np.zeros((size, size)).astype(np.uint8)
    for i in range(start[0],side):
    	for j in range(start[1],side):
    		image[i,j] = 255
    return image


"""
3 - Koło
"""
def midcircle(size):
    image = np.zeros((size[0], size[1])).astype(np.uint8)
    if (size[0] > size[1]):
    	r = size[1]//4
    else:
    	r = size[0]//4

    y0=size[0]/2
    x0=size[1]/2

    y,x = np.ogrid[0:size[0], 0:size[1]]
    mask = ((x-x0) **2 + (y-y0) ** 2) < r**2
    image[mask] = 255


    return image

"""
3 - Szachownica.
"""

def drawSquare(image, pos, leng, color):
	image[pos] = color
	for i in range(pos[0], pos[0]+leng):
		for j in range(pos[1], pos[1]+leng):
			image[i,j] = color


def checkerboard(size):
    image = np.zeros((size, size)).astype(np.uint8)

    cnt = 0

    for i in range(8):
    	for j in range(8):
    		pos = (size//8 * i, size//8 * j)
    		# print (pos)
    		if ((i%2 == 0 and j%2 == 1) or ((i%2 == 1 and j%2 == 0))):
    			drawSquare(image, pos, size//8, 255)

    return image

"""
4 - Interpolacja najbliższych sąsiadów.
"""
def nn_interpolation(source, new_size):
    pass

"""
5 - Interpolacja dwuliniowa
"""
def bilinear_interpolation(source, new_size):
    pass
