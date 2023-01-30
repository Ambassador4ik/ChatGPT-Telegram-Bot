class Message:
    raw_text: str
    has_implicit_attributes: bool = False
    raw_attributes: list[str] = []

    prompt: str = "An Error occured and reply was not generated."
    model: str = "text-davinci-003"
    temperature: float = 0.5
    max_tokens: int = 1000
    top_p: float = 1.0
    frequency_penalty: float = 0.5
    presence_penalty: float = 0.0

    has_errors: bool = False
    error_message: str = ""

    def __init__(self, text: str):
        self.raw_text = text
        self.parse_message()

    def parse_message(self):
        if "/attribs" in self.raw_text:
            attribs = Message.parse_attributes(self.raw_text.split("/attribs")[1])
            if len(attribs) > 0:
                self.has_implicit_attributes = True
                self.raw_attributes = attribs
                try:
                    self.validate_attributes()
                    self.prompt = self.raw_text.split("/attribs")[0]
                except BaseException as e:
                    self.has_errors = True
                    self.error_message = str(e)

        else:
            self.prompt = self.raw_text

    def validate_attributes(self):
        attrib_value_dict = {}
        for att in self.raw_attributes:
            parts = att.split("=")
            attrib_value_dict[parts[0]] = parts[1]
        valid_attrib_names = ["model", "temperature", "max_tokens", "top_p",
                              "frequency_penalty", "presence_penalty"]
        for key in attrib_value_dict:
            if key not in valid_attrib_names:
                raise ValueError("Unknown attribute")
            if key == "model":
                if attrib_value_dict[key] in ["text-davinci-003", "code-davinci-002", "text-curie-001",
                                              "text-babbage-001", "code-cushman-001", "text-ada-001"]:
                    self.model = attrib_value_dict[key]
                else:
                    raise ValueError("Invalid Model")
            elif key == "temperature":
                if 0 <= float(attrib_value_dict[key]) <= 1:
                    self.temperature = float(attrib_value_dict[key])
                else:
                    raise ValueError("Temperature should be float in [0, 1]")
            elif key == "max_tokens":
                if 1 <= int(attrib_value_dict[key]) <= 2000:
                    self.max_tokens = int(attrib_value_dict[key])
                else:
                    raise ValueError("Max-Tokens should be integer in [1, 2000]")
            elif key == "top_p":
                if 0 <= float(attrib_value_dict[key]) <= 1:
                    self.top_p = float(attrib_value_dict[key])
                else:
                    raise ValueError("Top P should be float in [0, 1]")
            elif key == "frequency_penalty":
                if 0 <= float(attrib_value_dict[key]) <= 2:
                    self.frequency_penalty = float(attrib_value_dict[key])
                else:
                    raise ValueError("Frequency penalty should be float in [0, 2]")
            elif key == "presence_penalty":
                if 0 <= float(attrib_value_dict[key]) <= 2:
                    self.presence_penalty = float(attrib_value_dict[key])
                else:
                    raise ValueError("Presence penalty should be float in [0, 2]")

    @staticmethod
    def parse_attributes(line: str):
        parts = line.split()
        attributes = []
        for part in parts:
            if part.startswith("--"):
                attributes.append(part[2:])
        return attributes
