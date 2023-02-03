class NotKenzieEmailError(Exception):
    default_message = "email precisa ser @kenzie.com"

    def __init__(self, message=None):
        self.message = message or self.default_message

        # if not message:
        #     self.message = self.default_message
        # else:
        #     self.message = message


def is_kenzie_domain(email: str):
    if not email.endswith("@kenzie.com"):
        raise NotKenzieEmailError("Uma nova mensagem de error")

