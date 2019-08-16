from PIL import Image
def invert (im):
    '''Invert  colors in im'''
    # Find the dimensions of the image
    (width, height) = im.size

    # Loop over the entire image
    for x in range( width ):
        for y in range( height ):
            (red, green, blue) = im.getpixel((x, y))
            #sets the pixel as each opposite RGB value
            im.putpixel((x, y),(255-red, 255-green, 255-blue))
            # Complete this function by adding your lines of code here.
            # You need to calculate the new pixel values and then to change them
            # in the image using putpixel()
def invert_block(im):
    (width, height) = im.size

    # Loop over the entire image
    for x in range( width//2 ):
        for y in range( height//2 ):
            (red, green, blue) = im.getpixel((x, y))
            #sets the pixel as each opposite RGB value
            im.putpixel((x, y),(255-red, 255-green, 255-blue))


bear = Image.open("bear.png")
print(bear.size)
pixel = bear.getpixel((100, 200))
print(pixel)
#for i in range(100):
#    for j in range(100):
#        bear.putpixel((i,j), (0,0,0))
invert_block(bear)
bear.show()
bear.save("scaryBear.jpg")


