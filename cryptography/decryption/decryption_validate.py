from cryptography.core.validate import Validate


class DecryptionValidate(Validate):
    """Класс для работы с валидностью перед декодировкой"""

    def is_valid_length(self, digit, max_length):
        """Проверка на длину"""
        digit_str = str(digit)
        result = len(digit_str) <= max_length
        if not result:
            self.helper_error_message.new_error(f"{digit} длина числа больше {max_length}")
        return result
