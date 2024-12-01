from PIL import Image

image = Image.open('dzhungli_les_debri_64072_1920x1080.jpg')
box = (0,0,64,64)
region = image.crop(box)
r, g, b= region.split()
region = Image.merge('RGB', (g, b, r))


box_2 = (64,64,128,128)
r, g, b= region.split()
region = Image.merge('RGB', (g, r, b))
image.paste(region, box_2)


box_3 = (64, 0, 128, 64)
region = image.crop(box_3)
region = region.rotate(45)
image.paste(region, box_3)

image.show()