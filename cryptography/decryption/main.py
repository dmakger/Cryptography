from cryptography.decryption.decryption import Decryption
from random import randint

if __name__ == '__main__':
    digits = list()
    for i in range(100):
        digits.append(randint(0, 9999))

    decryption = Decryption()
    for digit in digits:
        print(f"{digit} => {decryption.decrypt(digit)}")
