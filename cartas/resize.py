from PIL import Image

for i in range(9):
    image = Image.open("cartas/carta"+str(i)+".png")
    image = image.resize((150, 210), Image.ANTIALIAS)
    image.save('cartas/carta'+str(i)+'.png')