#Colton Swartwoudt

import numpy as np
import PIL
from PIL import Image, ImageDraw, ImageFilter, ImageOps

#baseline functionality is present, however there are some quirks that
#should be addressed

#issue 1, image was not detected unless absolute filepaths were used
#unsure how it will react to being in a git repository / put on another machine

#issue 2, ellipses did not generate concentric rings, but instead just
#created a diagonal line across the mask

def main():
    #Image Initialization
    print("Initializing")
    im1 = Image.open("C:/Users/Rebound/school/Code/Python/Week 3/testImage.png")
    im1 = im1.convert("RGB")
    im2 = Image.open("C:/Users/Rebound/school/Code/Python/Week 3/testImage.png")
    im2 = im2.convert("RGB")
    width = im1.size[0]
    height = im1.size[1]
    blankSet = np.zeros( (height, width) )

    #Image Filtering
    print("Applying Filters")
    im1 = ImageOps.grayscale(im1)
    im2 = im2.filter(ImageFilter.FIND_EDGES)

    #Mask Creation
    print("Generating Masks")
    i = 0
    numSlices = 8
    mask = Image.fromarray(blankSet, "RGBA")
    maskDrawer = ImageDraw.Draw(mask)
    for i in range(numSlices):
        maskDrawer.ellipse(
            #TODO: Fix ellipse generation code, see issue 2
            (i * width / numSlices, i * height / numSlices) #Inner Bound
            + ((i+1) * width / numSlices, (i+1) * height / numSlices), #Outer Bound
            fill = "black", outline = "black"
        )
    mask.show()

    #Composition
    print("Compositing Images")
    im3 = Image.composite(im1, im2, mask)
    im3.show()
    im3.save("diagonalMasks.png")


if __name__ == "__main__":
    main()