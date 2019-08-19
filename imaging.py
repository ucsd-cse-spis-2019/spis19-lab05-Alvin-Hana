#lab05 pair programming
from PIL import Image
def greyscale(im):
    #gets the width and height of picture
    (width, height) = im.size
    for x in range( width ):
        for y in range( height ):
            (red, green, blue) = im.getpixel((x, y))
            #sets the pixel as each opposite RGB value
            grey = green*.72+red*.21+blue*.07
            im.putpixel((x, y),(int(grey),int(grey), int(grey)))

bear = Image.open("bear.png")
greyscale(bear)
bear.show()


