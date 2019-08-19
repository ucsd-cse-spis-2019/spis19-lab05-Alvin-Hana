#lab05 pair programming
from PIL import Image
import random

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

def scale(im):
    (width, height) = im.size
    copyim = Image.new('RGB', (width//2,height//2))
    for x in range( width//2 ):
        for y in range( height//2 ):
            (red, green, blue) = im.getpixel((x*2, y*2))
            copyim.putpixel((x, y), (red, green, blue))
    return copyim


def blur(im):
    (width, height) = im.size
    copyim = Image.new('RGB', (width,height))
    for x in range( 0, width, 2 ):
        for y in range( 0, height, 2 ):
            (red1, green1, blue1) = im.getpixel((x, y))
            (red2, green2, blue2) = im.getpixel((x+1,y))
            (red3, green3, blue3) = im.getpixel((x+1,y+1))
            (red4, green4, blue4) = im.getpixel((x,y+1))
            avgRed = (red1+red2+red3+red4)//4
            avgGreen = (green1+green2+green3+green4)//4
            avgBlue = (blue1+blue2+blue3+blue4)//4
            copyim.putpixel((x, y), (avgRed, avgGreen, avgBlue))
            copyim.putpixel((x+1, y), (avgRed, avgGreen, avgBlue))
            copyim.putpixel((x+1, y+1), (avgRed, avgGreen, avgBlue))
            copyim.putpixel((x, y+1), (avgRed, avgGreen, avgBlue))
    return copyim

def randomGrid(im):
    (width, height) = im.size
    copyim = Image.new('RGB', (width,height))
    for x in range( 0, width, 100 ):
        for y in range( 0, height, 100 ):
            xRand = random.randrange(0, 6)
            yRand = random.randrange(0, 8)





bear = Image.open("bear.png")
#jaz = Image.open("jaz.jpg")
#binarize(bear,127, 0, 0, 600, 800)
#binarize(jaz,127, 0, 0, 700,950)
#curt = Image.open("curt.jpg")
#mirrorHoriz(jaz)
#bear.show()
#flipVert(jaz)
#mirrorHoriz(curt)
#flipVert(curt)
#curt.show()
newbear = randomGrid(bear)
bear.show()
newbear.show()
#jaz.save("coolest jaz.jpg")
#curt.save("cooler_curtz.jpg")
