class APIError(Exception):
    pass


class HTTPError(APIError):
    def __init__(self, message, response=None):
        super().__init__(message)
        self.response = response
