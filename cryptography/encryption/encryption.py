from cryptography.cryptography import Cryptography
from cryptography.encryption.encryption_validate import EncryptionValidate


class Encryption(Cryptography):
    def is_valid_encrypt(self, digit):
        """Проверка на валидность поступающего числа"""
        validator = EncryptionValidate()
        is_validate = validator.is_valid(digit=digit, max_length=self.MAX_LENGTH)
        if not is_validate:
            validator.print_error()
        return is_validate

    @staticmethod
    def encrypt_value(digit):
        """
        Каждому элементу числа добавляется 7 и делится с остатком на 10
        Input: 1234
        Output: '8901'
        """
        encrypt_str = ''
        for ch in str(digit):
            encrypt_str += f"{(int(ch) + 7) % 10}"
        return encrypt_str

    @staticmethod
    def encrypt_swap(digit_str):
        """
        Меняем 1ое число с 3им, и 2ое с 4ым
        Input: '1234'
        Output: '3421'
        """
        return f"{digit_str[2]}{digit_str[3]}{digit_str[0]}{digit_str[1]}"

    def encrypt(self, digit):
        """Перекодирование"""
        validate = self.is_valid_encrypt(digit=digit)
        if not validate:
            return False

        new_digit_str = self.encrypt_value(digit=digit)
        new_digit_str = self.encrypt_swap(digit_str=new_digit_str)
        return int(new_digit_str)
