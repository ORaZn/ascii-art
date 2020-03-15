from PIL import Image
import numpy as np
import os, sys
# open an image file (.bmp,.jpg,.png,.gif) you have in the working folder
imageFile = "zebra.jpg"
im1 = Image.open(imageFile)
# adjust width and height to your needs
width = 340
height = 380
# use one of these filter options to resize the image
im2 = im1.resize((width, height), Image.NEAREST)      # use nearest neighbour
im3 = im1.resize((width, height), Image.BILINEAR)     # linear interpolation in a 2x2 environment
im4 = im1.resize((width, height), Image.BICUBIC)      # cubic spline interpolation in a 4x4 environment
im5 = im1.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter
ext = ".jpg"
im2.save("NEAREST" + ext)
im3.save("BILINEAR" + ext)
im4.save("BICUBIC" + ext)
im5.save("ANTIALIAS" + ext)

image1 = np.asarray(Image.open("ANTIALIAS.jpg")) 
#print(image1.shape)
image2=np.asarray(Image.open("zebra.jpg"))
#print(image2.shape)
brightness_matrix=np.dot(image2,[1/3,1/3,1/3]) 

ascival="`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" 
ascii_matrix=np.zeros((188,267),dtype='U1')
for i in range(1,66):
    ascii_matrix[(brightness_matrix<i*(255/65)) & (brightness_matrix>=(i-1)*(255/65))]=ascival[i-1]

new_ascii_matrix=np.repeat(ascii_matrix,3,axis=1)

def print_array(arr):
    """
    prints a 2-D numpy array in a nicer format
    """
    for a in arr:
        for elem in a:
            print(elem, end="")
        print("\n")

print_array(new_ascii_matrix)
