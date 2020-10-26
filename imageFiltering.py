#Colton Swartwoudt

import numpy as np
import PIL
from PIL import Image, ImageDraw, ImageFilter, ImageOps

#issue 1, image was not detected unless absolute filepaths were used.
#Unsure how it will react to being in a git repository / put on another machine.
#However, this may be a non-issue once interfaced with Austin's code.

#issue 2, SOLVED
#Ellipses did not generate concentric rings, but instead just
#created a diagonal line across the mask.
#Instead of generating ellipses at i and i + 1, it was changed to
#generate at i and numSlices - i.

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
    numSlices = 16
    mask = Image.fromarray(blankSet, "RGBA")
    maskDrawer = ImageDraw.Draw(mask)
    color = ""
    for i in range(numSlices):
        if i % 2 == True:
            color = (0, 0, 0, 0) #Transparent
        else:
            color = (0, 0, 0, 255) #Black
        maskDrawer.ellipse(
            (i * width / numSlices, i * height / numSlices) #Top Left Corner of Ellipse
            + ( (numSlices - i) * width / numSlices, (numSlices - i) * height / numSlices ), #Bottom Right Corner of Ellipse
            fill = color, outline = color
            )
    mask.show()
    mask.save("mask.png")

    #Composition
    print("Compositing Images")
    im3 = Image.composite(im1, im2, mask)
    im3.show()
    im3.save("output.png")


if __name__ == "__main__":
    main()