from lfsr import LFSR
from PIL import Image, ImageColor

print(Image.__name__ + "was imported successfully")


def main():
    filename = "/Users/CaseyJayne/Downloads/football.png"
    outfile = "/Users/CaseyJayne/Downloads/football_encrypted.png"
    decryptfile = "/Users/CaseyJayne/Downloads/football_decrypted.png"
    lfsr = LFSR("10011010", 5)
    enc = ImageEncrypter(filename, lfsr, outfile, decryptfile)


class ImageEncrypter:

    def __init__(self, filename: str, lfsr: LFSR, out_location, decrypt_location):
        self.lfsr = lfsr  # a class object lfsr
        self.startlfsr = lfsr.seed
        pixels = self.parsefile(filename)
        # encrypt pixels
        enc_pixels = self.encrypt(pixels)
        # create encrypted image
        new = self.newImage(enc_pixels)
        new.save(out_location)  # save to file
        # decrypt
        self.lfsr.seed = self.startlfsr  # reset seed
        orig = self.decrypt(enc_pixels)
        decrypt = self.newImage(orig)
        decrypt.save(decrypt_location)
        # below: testing that it worked
        # print(pixels[0:5])
        # print(enc_pixels[0:5])
        # print(orig[0:5])
        # print(f"Original equals new? {pixels == orig}")
        # recreate & display image
        self.newImage(orig)

    def parsefile(self, filename):
        # read in the file and put it into a 2D array of components
        image = Image.open(filename)
        # display the input image
        image.show()
        # get the image pixels
        pixels = list(image.getdata())
        return pixels

    def getBin(self, seed: str):
        """
        get binary number from string
        """
        num = 0
        for i in range(1, len(seed) + 1):
            # add the binary digit if applicable
            value = int(seed[-i])
            if value:
                num += 2 ** (i - 1)
        return num

    def encrypt(self, image: list):
        enc_pixel = []
        for pixel in image:  # each tuple
            # print(f"Original pixel {pixel}")
            # R G and B in each
            self.lfsr.seed = self.lfsr.step()
            bin = self.getBin(self.lfsr.seed)
            # print(f"LFSR value {bin}")
            r = pixel[0] ^ bin
            self.lfsr.seed = self.lfsr.step()
            bin = self.getBin(self.lfsr.seed)
            # print(f"LFSR value {bin}")
            g = pixel[1] ^ bin
            self.lfsr.seed = self.lfsr.step()
            bin = self.getBin(self.lfsr.seed)
            # print(f"LFSR value {bin}")
            b = pixel[2] ^ bin
            colortup = (r, g, b)
            # print(f"New pixel: {colortup}")
            enc_pixel.append(colortup)

        # print(str(enc_pixel))
        return enc_pixel

    def newImage(self, image_colors):
        # create a new image
        new_image = Image.new("RGB", size=(225, 225))
        new_image.putdata(image_colors)
        # new_image.load(image_colors)
        new_image.show()
        return new_image

    def decrypt(self, image: list):
        return self.encrypt(image)


if __name__ == "__main__":
    main()
