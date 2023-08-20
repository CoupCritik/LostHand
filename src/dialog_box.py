import pygame
from pygame.locals import *
from utils import Vector2


BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
WHITE = (255,255,255)

WIDTH_BOX = 650
HEIGHT_BOX = 200


class DialogBox:
	def __init__(self, position: Vector2, text: str, scale: int, text_speed: int) -> None:
		self.position = position
		self.text = text
		self.scale = scale
		self.font = pygame.font.SysFont(None, self.scale)
		self.sentences_textures = []

		self.timer = 0
		self.wait_time = int(1 / text_speed * 100.0)
		self.current_word = 0
		self.text_end = False



	def load_text_textures(self) -> None:

		all_lines = []
		lower_bound = 0

		print("hello")

		for i in range(len(self.text)):
			print("test" + str(i))

			line_texture = self.font.render(self.text[lower_bound:i+1], True, WHITE)
			text_texture = pygame.Surface((WIDTH_BOX, HEIGHT_BOX), pygame.SRCALPHA)

			total_height = 0

			for j, line in enumerate(all_lines):
				total_height = total_height + self.scale
				end_texture.blit(line, (0, total_height))

			# limit of the dialogbox
			if line_texture.get_width() >= WIDTH_BOX:
				lower_bound = i + 1
				all_lines.append(line_texture)

			text_texture.blit(line_texture, (0, total_height + 20))

			self.sentences_textures.append(text_texture)


	def get_texture(self):

		if self.timer < self.wait_time:
			self.timer = self.timer + 1

		if self.timer == self.wait_time and self.current_word < len(self.sentences_textures) - 1:
			self.timer = 0

			if not self.text_end:
				self.current_word = self.current_word + 1

		self.text_end = (self.current_word == len(self.sentences_textures) - 1)

		return self.sentences_textures[self.current_word]


	def draw_dialog_box(self, window_texture) -> None:
		window_texture.blit(self.get_texture(), (self.position.x, self.position.y))