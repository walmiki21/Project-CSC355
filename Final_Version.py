#Group 4: Colton Swartwoudt, Austin Kim, Alex Heisdorffer, Walmiki Kanuru
#October 28 2020
#CSC 355
#Final Assignment

#import functions
import numpy as np
import PIL
from PIL import Image, ImageDraw, ImageFilter, ImageOps
from tkinter import *
from PIL import ImageTk,Image
from tkinter import colorchooser

root = Tk()
root.title( 'Image' )
root.geometry("500x1000") #Original dimensions of original image
root.iconbitmap('C:/Users/atk41/OneDrive/Documents/windowsreport-logo.png')

#imported photos
my_img = ImageTk.PhotoImage(Image.open('C:/Users/atk41/OneDrive/Documents/windowsreport-logo.png'))
my_label = Label(image=my_img)
my_label.pack()

#resize function
def resize():
    w = width_entry.get()
    h = height_entry.get()
    #f string to substitute the w and h above
    root.geometry(f"{w}x{h}")

#pass for user generated width
width_label = Label(root, text="Width:")
width_label.pack(pady=15)
width_entry = Entry(root)
width_entry.pack()

#pass for user generated height
height_label = Label(root, text="Height:")
height_label.pack(pady=15)
height_entry = Entry(root)
height_entry.pack()

#only have this thing fire when we want it to.
def color():
    my_color = colorchooser.askcolor()[1]#[]designate which one we want.
    #what is the colorchooser returning to us?
    my_label = Label(root, text=my_color).pack(pady=10)
    my_label2 = Label(root,image=my_img, bg=my_color).pack()

 #Button options for resizing and colors   
my_button = Button(root, text="Resize", command=resize)
my_button.pack(pady=20)
my_button = Button(root, text="Color", command=color).pack()
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()

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
    
   #The color and pattern of the photo
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
