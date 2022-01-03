from PIL import Image
import sys
import os

original_folder = sys.argv[1]
new_folder = sys.argv[2]

images = os.listdir(f'{original_folder}')
images.remove(".DS_Store")  # i don't know why it was there

os.mkdir(f'{new_folder}')
for image in images:
    im = Image.open(f"{original_folder}{image}")
    middle = image.split(".")
    name = middle[0]
    im_in_png = im.save(f'{new_folder}{name}.png', 'png')
