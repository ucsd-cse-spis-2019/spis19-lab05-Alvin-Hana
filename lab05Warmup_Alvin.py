from PIL import Image
bear = Image.open( "bear.png" )
#prints number of pixels
print (bear.size)
pixel = bear.getpixel( ( 100, 200) )
print(pixel)
#for i in range(100):
    #bear.putpixel( (i, 200) , (0, 0, 0) )
def invert( im ):
    #''' Invert the colors in the input image, im '''
    # Find the dimensions of the image
    (width, height) = im.size
    # Loop over the entire image
    for x in range( width ):
        for y in range( height ):
            (red, green, blue) = im.getpixel((x, y))
            # Complete this function by adding your lines of code here.
            # You need to calculate the new pixel values and then to change them
            # in the image using putpixel()
            im.putpixel( (x, y) , (255-red, 255-green, 255-blue) )

def invert_block( im ):
    (width, height) = im.size
    for x in range( width//2 ):
        for y in range( height//2 ):
            (red, green, blue) = im.getpixel((x, y))
            # Complete this function by adding your lines of code here.
            # You need to calculate the new pixel values and then to change them
            # in the image using putpixel()
            im.putpixel( (x, y) , (255-red, 255-green, 255-blue) )


invert (bear)
invert_block(bear)
bear.show()
#bear.save ("bearInverted.jpg")

