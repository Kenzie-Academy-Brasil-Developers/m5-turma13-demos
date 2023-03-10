class NotFoundError(Exception):
    status_code = 404
    default_message = "Not Found."

    def __init__(self, message=None) -> None:
        self.message = message or self.default_message
