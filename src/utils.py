class Vector2:
	def __init__(self, x: float, y: float) -> None:
		self.x = x
		self.y = y
	def __str__(self):
		return f'({self.x},{self.y})'

class Vector2i:
	def __init__(self, x: int, y: int) -> None:
		assert type(x)==int and type(y)==int,"Les paramètres ne sont pas entiers"
		self.x = x
		self.y = y
	def __str__(self):
		return f'({self.x},{self.y})'
