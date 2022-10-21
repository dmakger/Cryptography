from cryptography.error_message import ErrorMessage


class Validate:

    def __init__(self):
        self.helper_error_message = ErrorMessage()
        self.result = None

    def print_error(self):
        """Вывод всех ошибок текстом"""
        print("========== ERROR ==========")
        print(self.helper_error_message.get_error())
        print("===========================")

    def is_valid_type(self, digit):
        """Проверка на тип"""
        result = type(digit) == int
        if not result:
            self.helper_error_message.new_error(f"{digit} не является числом")
        return result

    def is_valid(self, digit, max_length):
        """Полная проверка"""
        valid_type = self.is_valid_type(digit=digit)
        valid_length = self.is_valid_length(digit=digit, max_length=max_length)
        self.result = valid_type and valid_length
        return self.result
