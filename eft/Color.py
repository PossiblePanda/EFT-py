class EFT_Color:
	def __init__(self, r, g, b, a=255):
		self.r = r
		self.g = g
		self.b = b
		self.a = a

	def to_hex(self):
		return "#{:02x}{:02x}{:02x}".format(self.r, self.g, self.b)

	def to_rgb(self):
		return (self.r, self.g, self.b)

	def to_rgba(self):
		return (self.r, self.g, self.b, self.a)

	def set_alpha(self, alpha):
		self.a = alpha

	def invert(self):
		self.r = 255 - self.r
		self.g = 255 - self.g
		self.b = 255 - self.b

	def grayscale(self):
		average = (self.r + self.g + self.b) // 3
		self.r = average
		self.g = average
		self.b = average
	
	def brighten(self, value):
		"""
		Increase the brightness of the color by the specified value.
		
		Parameters:
		- value (int): The value by which to increase the brightness.
		
		Returns:
		None
		"""
		self.r = min(self.r + value, 255)
		self.g = min(self.g + value, 255)
		self.b = min(self.b + value, 255)

	def darken(self, value):
		"""
		Decrease the brightness of the color by the specified value.
		
		Parameters:
		- value (int): The value by which to decrease the brightness.
		
		Returns:
		None
		"""
		self.r = max(self.r - value, 0)
		self.g = max(self.g - value, 0)
		self.b = max(self.b - value, 0)

	def blend(self, color, alpha):
		"""
		Blend the color with another color using the specified alpha value.
		
		Parameters:
		- color (EFT_Color): The color to blend with.
		- alpha (float): The alpha value for blending (0.0 - 1.0).
		
		Returns:
		None
		"""
		self.r = int(self.r * (1 - alpha) + color.r * alpha)
		self.g = int(self.g * (1 - alpha) + color.g * alpha)
		self.b = int(self.b * (1 - alpha) + color.b * alpha)

	def __str__(self):
		"""
		Return a string representation of the color.
		
		Returns:
		str: The string representation of the color.
		"""
		return "EFT_Color({}, {}, {})".format(self.r, self.g, self.b)
		