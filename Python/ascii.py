import math
from PIL import Image
import numpy as np

ASCII = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

ascii_len = len(ASCII)

im = Image.open("joker.png")
im = im.convert('RGB')
im = im.resize((int(im.size[0]*0.1), int(im.size[1]*0.1)))

print(im.format, im.size, im.mode)

width, height = im.size

pix_arr = im.load()

print(pix_arr[0, 0])

# Convert RGB to brightness values using average r+b+g/3

brightness_arr = [[0] * height for i in range(width)]  # empty 2d array maybe

for h in range(height - 1):
    for w in range(width - 1):
        r, g, b, = pix_arr[w, h]
        brightness_arr[w][h] = (r + g + b) / 3

arr = np.array(brightness_arr)
# print(arr.max(), arr.min())

# Map each brightness value to an ascii char

values_per_char = 255 / ascii_len

ascii_arr = [[0] * height for i in range(width)]

for h in range(height - 1):
    for w in range(width - 1):
        ascii_arr[w][h] = ASCII[math.ceil(brightness_arr[w][h] / values_per_char)]

# print that shit

for h in range(height - 1):
    for w in range(width - 1):
        print(ascii_arr[w][h], end="")
        print(ascii_arr[w][h], end="")
        print(ascii_arr[w][h], end="")
    print()
