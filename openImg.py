from PIL import Image
pil_im = Image.open('empire.jpg')
pil_im_Gray = Image.open('empire.jpg').convert('L')
pil_im_Gray.save('empire_gray.jpg')
