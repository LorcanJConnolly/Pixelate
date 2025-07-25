from PIL import Image
import numpy as np

image = Image.open('src\main\python\domain\img2.jpeg')
image.convert(mode="RGB")

pixels = image.load()
imagex, imagey = image.size

pixels_per_group = 100

average_rgb = None
new_image = {}

for y in range(imagey):
    for x in range(imagex): 
        if x*y != 0 and x % pixels_per_group == 0 and y % pixels_per_group == 0:
            # if average_value tuple contains a value larger than 255 we have a problem
            new_image[tuple([x, y])] = average_rgb 
            average_rgb = None
        else:
            if average_rgb:
                tuples = [average_rgb, pixels[x,y]]
                average_rgb = tuple(map(lambda two_dp: int(round(two_dp, 2)), np.mean(tuples, axis=0))) 
            else:
                average_rgb = pixels[x, y]

print(new_image)