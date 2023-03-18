class GedcomParser():

    path: str

    def __init__(self, path: str):
        self.path = path

    def __open(self) -> str:
        with open(self.path, "r") as file:
            data = file.read()
        return data
    
    def __parse_line(self, line: str) -> dict:
        level = int(line[0])
        tag = line[2:6]
        value = line[7:]
        return {"level": level, "tag": tag, "value": value}

    def verify(self) -> dict:
        file = self.__open()
        lines = file.split('\n')
        current_level = 0
        current_line = 0
        for line in lines:
            current_line += 1
            if line != "":
                # Check if the level is valid
                parsed_line = self.__parse_line(line)
                if parsed_line["level"] > current_level + 1:
                    return {"status": "error", "message": "Invalid level on line " + str(current_line) + ": " + line}
                current_level = parsed_line["level"]
        return {"status": "ok", "message": ""}