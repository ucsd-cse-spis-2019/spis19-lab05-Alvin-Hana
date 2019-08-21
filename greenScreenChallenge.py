from PIL import Image
def removeGreen(im, bg):
    #gets the width and height of picture
    (width, height) = im.size
    for x in range( width ):
        for y in range( height ):
            (red, green, blue) = im.getpixel((x, y))
            if green<80 or red>90 or blue>160:
                bg.putpixel((x+90,y+80),(red,green,blue))
                
def scale(im):
    (width, height) = im.size
    copyim = Image.new('RGB', (width//8,height//8))
    for x in range( width//8 ):
        for y in range( height//8 ):
            (red, green, blue) = im.getpixel((x*8, y*8))
            copyim.putpixel((x, y), (red, green, blue))
    return copyim




face=Image.open("coolerJaz.jpg")
newFace=scale(face)
bee=Image.open("bee.jpg")
#shrek=Image.open("shrek.jpg")
removeGreen(newFace, bee)
bee.show()
bee.save("JazLikesJazz.jpg")

#face=Image.open("coolerJaz.jpg")
#bee=Image.open("bee.jpg")
#newFace=scale(face)
#bee.show()
#bee=Image.open("bee.jpg")
#removeGreen(face, bee)
#bee.show()
#faces=Image.open("faces.jpg")
#newFaces=scale(faces)
#shrek=Image.open("shrek.jpg")
#removeGreen(newFaces, shrek)
#shrek.show()
#shrek.save("jaz's family.jpg")
#(red, green, blue) = faces.getpixel((0, 2600))
#print(red)
#print(green)
#print(blue)

