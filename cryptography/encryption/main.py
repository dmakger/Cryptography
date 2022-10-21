from cryptography.encryption.encryption import Encryption
from random import randint

if __name__ == '__main__':
    digits = list()
    for i in range(100):
        digits.append(randint(1000, 9999))

    encryption = Encryption()
    for digit in digits:
        print(f"{digit} => {encryption.encrypt(digit)}")


