class Theme:
    def __init__(self, path: str):
        self.theme_path = path
        self.file_contents = open(path, 'r').read()
        self.lines = self.file_contents.split('\n')
        self.dict = {"name": "", "properties": {}, "groups": {}}

        current_group = None
        for line in self.lines:
            split = line.split(":")
            if line.startswith("-"):
                self.dict["name"] = _format(line.removeprefix("-"))
            elif line.startswith("{"):
                current_group = _format(line.removeprefix("{").removesuffix("}"))
                self.dict["groups"][current_group] = {}
            elif len(split) >= 3:
                property_dict = {
                    "raw_value": _format(split[1]),
                    "type": _format(split[2]),
                    "value": _get_object_from_type_value(_format(split[1]), _format(split[2]))
                }
                if current_group is None:
                    self.dict["properties"][_format(split[0])] = property_dict
                else:
                    self.dict["groups"][current_group][_format(split[0])] = property_dict

    def get_property(self, name: str):
        if "/" in name:
            group_name, property_name = name.split("/")
            if group_name in self.dict["groups"] and property_name in self.dict["groups"][group_name]:
                return self.dict["groups"][group_name][property_name]["value"]
        elif self.has_property(name):
            return self.dict["properties"][name]["value"]
        return None

    def has_property(self, name: str) -> bool:
        return name in self.dict["properties"]

    # ... rest of your Theme methods ...

# Usage:
theme = Theme("MyTheme")
print(theme.get_property("GroupName/background_color"))  # Outputs: 255,255,255