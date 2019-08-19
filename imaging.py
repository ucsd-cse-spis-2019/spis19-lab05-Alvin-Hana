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


def binarize(im, thresh, startx, starty, endx, endy):
    (width, height) = im.size
    if startx < 0 or starty < 0 or endx > width or endy > height:
        print("Warning: That's illegal and I just called 911, have fun in jail!")
    else:
        for x in range( startx, endx ):
            for y in range( starty, endy ):
                (red, green, blue) = im.getpixel((x, y))
            #sets the pixel as each opposite RGB value
                grey = green*.72+red*.21+blue*.07
                if grey < thresh:
                    im.putpixel((x, y),(0, 0, 0))
                else:
                    im.putpixel((x, y),(255,255,255))

def mirrorVert(im):
    #gets the width and height of picture
    (width, height) = im.size
    for x in range( width ):
        for y in range( height//2 ):
            (red, green, blue) = im.getpixel((x, y))
            im.putpixel(((x),(height-y-1)),(red, green, blue))

def mirrorHoriz(im):
    #gets the width and height of picture
    (width, height) = im.size
    for x in range( width//2 ):
        for y in range( height):
            (red, green, blue) = im.getpixel((x, y))
            im.putpixel(((width-x-1),(y)),(red, green, blue))

def flipVert(im):
#gets the width and height of picture
    (width, height) = im.size
    for x in range( width ):
        for y in range( height//2 ):
            #creates variables for color on upper half pixels
            (red, green, blue) = im.getpixel((x, y))
            #creates color variables on lower half pixels
            (upperred, uppergreen, upperblue) = im.getpixel((x, height-y-1))
            #swaps colors of the two pixels
            im.putpixel(((x),(height-y-1)),(red, green, blue))
            im.putpixel (((x),(y)),(upperred, uppergreen, upperblue))

            

bear = Image.open("bear.png")
jaz = Image.open("jaz.jpg")
#binarize(bear,127, 0, 0, 600, 800)
#binarize(jaz,127, 0, 0, 700,950)
curt = Image.open("curt.jpg")
#mirrorHoriz(jaz)
#bear.show()
#flipVert(jaz)
mirrorHoriz(curt)
flipVert(curt)
curt.show()
#jaz.save("coolest jaz.jpg")
curt.save("cooler_curtz.jpg")
