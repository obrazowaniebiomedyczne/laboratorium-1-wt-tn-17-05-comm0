import numpy as np
from solution import *
from obpng import write_png
from obpng import read_png

# Dostateczna
print("- Ocena dostateczna")

## Kwadrat
print("  kwadrat")
image = square(512, 128, (32, 64))
write_png(image, 'results/1_square.png')

# Kółko

print("  kółka")
image = midcircle((512, 256))
write_png(image, 'results/2_circle_1.png')
image = midcircle((256, 512))
write_png(image, 'results/2_circle_2.png')
image = midcircle((512, 512))
write_png(image, 'results/2_circle_3.png')


# Szachownica

print("  szachownica")
image = checkerboard(256)
write_png(image, 'results/3_checkerboard.png')


# Dobra
lenna = np.squeeze(read_png('data/mono/lenna.png'))

## Interpolacja NN

print("- Ocena dobra")
print("  interpolacja najbliższych sąsiadów")
image = nn_interpolation(lenna, (100, 100))
image = nn_interpolation(image, (512, 512))
write_png(image, 'results/4_nn.png')


## Interpolacja dwuliniowa
"""
print("- Ocena bardzo dobra")
print("  interpolacja dwuliniowa")
image = bilinear_interpolation(lenna, (100, 100))
image = nn_interpolation(image, (512, 512))
write_png(image, 'results/5_bilinear.png')
"""
