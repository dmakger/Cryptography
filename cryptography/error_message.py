class ErrorMessage:

    def __init__(self):
        self.error = list()

    def error_exists(self):
        """Существуют ли ошибки"""
        return bool(self.error)

    def new_error(self, error):
        """Добавление новой ошибки"""
        self.error.append(error)

    def get_error(self):
        """Получение всех ошибок в виде текста разделенного ENTERом """
        return "\n".join(self.error)
