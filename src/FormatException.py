class FormatException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


known_formats = ["json"]
