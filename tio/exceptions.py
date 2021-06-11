class LangNotFound(Exception):
    def __init__(self, message="Unable to find this language"):
        self.message = message

        super().__init__(self.message)


class WrappingNotFound(Exception):
    def __init__(self, message="Unable to find a template for this language"):
        self.message = message

        super().__init__(self.message)


class TioError(Exception):
    def __init__(self, message="tio.run returned a incomprehensible response"):
        self.message = message

        super().__init__(self.message)
