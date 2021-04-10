'''
Created on Mar 30, 2021

@author: CaseyJayne
'''

from lfsr import LFSR
from PIL import Image, ImageColor
print(Image.__name__ + "was imported successfully")

def main():
    filename = "/Users/CaseyJayne/Downloads/football.png"
    lfsr = LFSR("10011010", 5)
    enc = ImageEncrypter(filename, lfsr)


class ImageEncrypter:

    def __init__(self, filename: str, lfsr: LFSR):
        self.parsefile(filename)
        self.lfsr = lfsr  # a class object lfsr
        self.startlfsr = lfsr

    def parsefile(self, filename):
        # read in the file and put it into a 2D array of components
        image = Image.open(filename)
        # display the input image
        image.show()
        # get the image pixels
        pixels = list(image.getdata())
        self.encrypt(pixels)

    def encrypt(self, image: list):
        enc_pixel = []
        for pixel in range(0, 5):  #image:  # each tuple
            # R G and B in each
            print(self.lfsr.seed)
            print(str(pixel[0]))
            r = pixel[0] ^ int(self.lfsr.seed)
            self.lfsr = self.lfsr.step()
            g = pixel[1] ^ int(self.lfsr.seed)
            self.lfsr = self.lfsr.step()
            b = pixel[2] ^ int(self.lfsr.seed)
            self.lfsr = self.lfsr.step()
            colortup = tuple(r, g, b)
            print(enc_pixel[pixel])
            print(colortup)
            enc_pixel.append(colortup)

        print(str(enc_pixel))
        # create encrypted image

    def newImage(self, image_colors):
        # create a new image
        new_image = Image.new("RGB", size=(256, 256), color=image_colors)
        new_image.show()
        return new_image

    def decrypt(self, image: list):
        self.encrypt(image)


if __name__ == '__main__':
    main()