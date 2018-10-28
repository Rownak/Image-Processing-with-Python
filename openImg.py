from PIL import Image
from pylab import *
pil_im = Image.open('empire.jpg')
pil_im_Gray = Image.open('empire.jpg').convert('L')
pil_im_Gray.save('empire_gray.jpg')
box = (100,100,200,200)
region = pil_im_Gray.crop(box)
region = region.transpose(Image.ROTATE_180)
pil_im_Gray.paste(region,box)
pil_im_Gray.save('empire_gray_rotate.jpg')