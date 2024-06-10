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
			if split.length >= 3:
				self.dict["properties"][split[0]] = {
					"raw_value": _format(split[1]),
					"type": _format(split[2]),
					"value": _get_object_from_type_value(_format(split[1]), _format(split[2]))
				}
			if line.begins_with("-"):
				self.dict["name"] = _format(line.erase(0))
	
	def get_dist(self) -> dict:
		return self.dict
	
	def get_theme_name(self) -> str:
		return self.dict["name"]
	
	def get_property(self, name: str):
		if self.has_property(name):
			return self.dict["properties"][name]
		return None
	
	def has_property(self, name: str) -> bool:
		return name in self.dict["properties"]

def _format(string: str) -> str:
	if string.begins_with(" "):
		string = string.erase(0)
	if string.ends_with(" "):
		string = string.erase(str.length() - 1)
	
	string = string.replace("\r", "")
	
	return string

def _get_object_from_type_value(raw_value: str, type: str):
	if type == "Int":
		return int(raw_value)
	elif type == "String":
		return raw_value.replace('"', "")
	
	print("Unknown value type: %s" % type)
	return None