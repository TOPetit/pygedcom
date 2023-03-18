class Element():
    def __init__(self, level: int, tag: str, value: str, sub_elements: list = []):
        self.level = level
        self.tag = tag
        self.value = value
