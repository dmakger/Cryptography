from cryptography.cryptography import Cryptography
from cryptography.decryption.decryption_validate import DecryptionValidate


class Decryption(Cryptography):
    @staticmethod
    def decrypt_value(code_str):
        """
        От каждого числа отнимается 7 и делится с остатком на 10
        Input: '8901'
        Output: '1234'
        """
        decrypt_str = ''
        for ch in code_str:
            value = int(ch) - 7
            if value < 0:
                value += 10
            decrypt_str += f"{value * 10 // 10}"
        return decrypt_str

    def get_code_str(self, code):
        code_zero_str = '0' * (self.MAX_LENGTH - len(str(code)))
        return f"{code_zero_str}{code}"

    def decrypt_swap(self, code):
        """
        Меняем 1ое число с 3им, и 2ое с 4ым
        Input: '1234'
        Output: '3421'
        """
        code_str = self.get_code_str(code=code)
        return f"{code_str[2]}{code_str[3]}{code_str[0]}{code_str[1]}"

    def is_valid_decrypt(self, code):
        """Проверка на валидность поступающего числа"""
        validator = DecryptionValidate()
        is_validate = validator.is_valid(digit=code, max_length=self.MAX_LENGTH)
        if not is_validate:
            validator.print_error()
        return is_validate

    def decrypt(self, code):
        """Декодирование"""
        validate = self.is_valid_decrypt(code=code)
        if not validate:
            return False

        new_code_str = self.decrypt_swap(code=code)
        new_code_str = self.decrypt_value(code_str=new_code_str)
        return int(new_code_str)
