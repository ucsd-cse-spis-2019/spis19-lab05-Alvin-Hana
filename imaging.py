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
    print(width)
    print(height)
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
                    im.putpixel((x, y), (255,255,255))



bear = Image.open("bear.png")
binarize(bear,127, 0, 0, 600, 800)
bear.show()

