from PIL import Image
def removeGreen(im, bg):
    #gets the width and height of picture
    (width, height) = im.size
    for x in range( width ):
        for y in range( 100, height ):
            (red, green, blue) = im.getpixel((x, y))
            if green<80 or red>90 or blue>160:
                bg.putpixel((x+205,y+36),(red,green,blue))
                
def scale(im):
    (width, height) = im.size
    copyim = Image.new('RGB', (width//13,height//13))
    for x in range( width//13 ):
        for y in range( height//13 ):
            (red, green, blue) = im.getpixel((x*13, y*13))
            copyim.putpixel((x, y), (red, green, blue))
    return copyim


faces=Image.open("faces.jpg")
newFaces=scale(faces)
shrek=Image.open("shrek.jpg")
removeGreen(newFaces, shrek)
shrek.show()
shrek.save("jaz's family.jpg")
#(red, green, blue) = faces.getpixel((0, 2600))
#print(red)
#print(green)
#print(blue)

