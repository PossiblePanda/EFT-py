from eft import Color
types = {}

class EFT_Theme():
	def __init__(self, path: str):
		self.dict = {
		"name": "Unknown Theme Name",
		"properties": {}
		}
				
		self.theme_path = path
		self.file_contents = open(path, 'r').read()
		self.lines = self.file_contents.split('\n')

		for line in self.lines:
			split = line.split(":")
			if len(split) >= 3:
				self.dict["properties"][_format(split[0])] = {
					"raw_value": _format(split[1]),
					"type": _format(split[2]),
					"value": _get_object_from_type_value(_format(split[1]), _format(split[2]))
				}
			if line.startswith("-"):
				self.dict["name"] = _format(line.removeprefix("-"))
	
	def get_dict(self) -> dict:
		return self.dict
	
	def get_theme_name(self) -> str:
		return self.dict["name"]
	
	def get_property(self, name: str):
		if self.has_property(name):
			return self.dict["properties"][name]["value"]
		return None
	
	def has_property(self, name: str) -> bool:
		return name in self.dict["properties"]

def _format(string: str) -> str:
	string = string.removeprefix(" ").removesuffix(" ")
	
	string = string.replace("\r", "")
	
	return string


def _get_object_from_type_value(raw_value: str, type: str):
	if type in types:
		return types[type](raw_value)
	
	print("Unknown value type: %s" % type)
	return None


def register_type(name: str, callback: callable):
	types[name] = callback


def _string(raw_value: str) -> str:
	return raw_value.replace('"', "")

def _int(raw_value: str) -> int:
	return int(raw_value)

def _bool(raw_value: str) -> bool:
	return raw_value.lower() == "true" or raw_value.lower() == "1"

def _color(raw_value: str) -> Color.EFT_Color:
	split = raw_value.split(",")
	color : Color.EFT_Color
	if len(split) == 4:
		color = Color.EFT_Color(int(split[0]), int(split[1]), int(split[2]), int(split[3]))
	else:
		color = Color.EFT_Color(int(split[0]), int(split[1]), int(split[2]))
	
	return color

# Register default types
register_type("String", _string)
register_type("Int", _int)
register_type("Color", _color)
register_type("Bool", _bool)