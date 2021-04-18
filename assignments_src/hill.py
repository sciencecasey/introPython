import numpy as np
import string


class SizeError(Exception):
    pass


class HillCyper:
    def __init__(self, text: str, mat: np.array, modulus: int, encrypt=True):
        if not isinstance(text, str):
            print("Text must be string type")
            return
        if not mat.__class__ == "ndarray":
            if not isinstance(mat, list):
                print("Matrix must be a numpy array or list")
                return
            try:
                mat = np.array(mat)  # convert to numpy array
            except TypeError:
                print("Input must be integer or float")
                return
        if not isinstance(modulus, int):
            print("Modulus must be an integer")
            return
        # grab inputs
        self.__key_matrix = mat
        self.__modulo = modulus
        self.__input_text = text
        self.__key_inv = self.mod_inverse()
        if isinstance(self.__key_inv, np.ndarray):
            if encrypt:
                self.encrypted_text = self.encrypt()
            else:
                self.decrypted_text = self.decrypt()

    def determinant(self):
        """
        returns the determinant of a matrix as a ndarray
        """
        mat = self.__key_matrix
        if mat.shape == (2, 2):
            a, b = mat[0, :]
            c, d = mat[1, :]
            det = a * d - b * c
            return det
        return mat.linalg.det()

    def invertible(self):
        """
        returns boolean if matrix is invertible
        """
        mat = self.__key_matrix
        row, col = mat.shape
        if row != col:
            print("Non-square matrix can't be inverted")
            return False
        det = self.determinant()
        if det == 0:
            print("Zero determinant, not invertible")
            return False
        return True

    def mod_inverse_scalar(self, scalar):
        """
        used: https://math.stackexchange.com/questions/3448234/
        calculating-modular-multiplicative-inverse-for-negative-values-of-a
        as a math reference to write
        """
        # scalar_inv = (self.__modulo + 1) / scalar
        if scalar != abs(scalar):
            scalar_inv = 1
            while (scalar_inv + self.__modulo*scalar_inv) * scalar % self.__modulo != 1:
                scalar_inv += 1
        else:
            scalar_inv = 1
            while scalar_inv * scalar % self.__modulo != 1:
                scalar_inv += 1
        return scalar_inv

    def mod_inverse(self):
        """"
        checks if matrix is invertible and if so returns the modular inverse
        """
        mat = self.__key_matrix
        try:
            if self.invertible():
                a, b = mat[0, :]
                c, d = mat[1, :]
                _ = np.array([[d, - b], [-c, a]])
                inv_det = self.mod_inverse_scalar(self.determinant())
                inv = inv_det * _ % self.__modulo
                return inv
            else:
                raise SizeError
        except SizeError:
            print("Not invertible matrix!")
            return

    def convert_numeric(self):
        # create the map
        letters = list(string.ascii_lowercase)
        nums = list(range(0, 26))
        mapping = dict(zip(letters, nums))
        # convert the input
        converted = list()
        for letter in self.__input_text:
            converted.append(mapping[letter])
        converted = np.array(converted)
        # separate into 2 rows
        converted = converted.reshape(int(converted.size / 2), 2)
        # print("Numeric Array:\n" + str(converted.T))
        return converted.T

    def convert_string(self, num_mat):
        # create the map
        letters = tuple(string.ascii_lowercase)  # indeces as keys
        converted = ""
        for row in num_mat.T:
            for number in row:
                converted += letters[int(number)]
        return converted

    def encrypt(self):
        conv_numeric = self.convert_numeric()
        print("Original matrix as numeric:\n" + str(conv_numeric))
        key = self.__key_matrix
        enc = np.dot(key, conv_numeric) % self.__modulo
        print("Encrypted Matrix:\n" + str(enc))
        enc_text = self.convert_string(enc)
        print("Encrypted String: " + enc_text)
        return enc_text

    def decrypt(self):
        dec_num = self.convert_numeric()
        # print(f"Decrypted Matrix:\n {dec_num}")  # should match the encrypted matrix
        key_inv = self.__key_inv
        dec_num = np.dot(key_inv, dec_num) % self.__modulo
        print(f"Decrypted Matrix:\n {dec_num}")
        dec_text = self.convert_string(dec_num)
        print("Decrypted text: " + dec_text)
        return dec_text


if __name__ == "__main__":
    TEXT = "attackatdawn"
    try:
        K = [[19, 8, 4],
             [3, 12, 7]]
        encrypted = HillCyper(text=TEXT, mat=K, modulus=26)
        decrypted = HillCyper(text=encrypted.encrypted_text, mat=K, modulus=26, encrypt=False)
    except AttributeError:
        print("Continuing to next attempt")
    try:
        K = [[7, 8],
             [11, 11]]
        encrypted = HillCyper(text=TEXT, mat=K, modulus=26)
        decrypted = HillCyper(text=encrypted.encrypted_text, mat=K, modulus=26, encrypt=False)
    except AttributeError:
        print("Continuing to next attempt")
    try:
        K = [[5, 15],
             [4, 12]]
        encrypted = HillCyper(text=TEXT, mat=K, modulus=26)
        decrypted = HillCyper(text=encrypted.encrypted_text, mat=K, modulus=26, encrypt=False)
    except AttributeError:
        print("Finished")
