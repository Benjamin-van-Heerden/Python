from PIL import Image
import os 

print('---')
print(os.listdir("example_images"))
print('---')

if not os.path.exists("./reworked"):
    os.makedirs("./reworked")

for file in os.listdir("example_images"):
    print(file)
    if file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".jpg"):

        im = Image.open(os.path.join("./example_images", file))
        new_im = im.rotate(-90).resize((128,128))
        path = ''.join(file.split('.')[:-1]) + ".png"
        new_im.save(os.path.join("./reworked", path))
