from PIL import Image
import numpy as np
import sys
import os


nombre = str(sys.argv[1])
im = Image.open(sys.argv[1])
im = im.convert('RGBA')
data = np.array(im)
red, green, blue, alpha = data.T
white_areas = (red == 238) & (blue == 238) & (green == 238)
data[..., :-1][white_areas.T] = (255,255,255)

im2 = Image.fromarray(data)
im2.save('./cuts/cut-'+nombre+'.png')
im.close()
