from PIL import Image

im = Image.open("./example_images/cancer_machine.jpeg")
new_im = im.resize((640,480))
new_im.save("./example_images/resized_cancer_machine.png")

im = Image.open("./example_images/resized_cancer_machine.png")
im.show()