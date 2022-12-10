import pygame


class Label:
    def __init__(self, surface, content: str, font: pygame.font.Font,
                 color: tuple[int, int, int] = (255, 255, 255)):  # Default color is white
        self.content = content
        self.font = font
        self.color = color
        self.label = None
        self.__create()
        self.surface = surface
        self.surface_width, self.surface_height = self.surface.get_size()
        self.blitted = False
        self.x = 0
        self.y = 0

    def __create(self):
        self.label = self.font.render(self.content, True, self.color)

    def set_content(self, content: str):
        self.content = content
        self.__create()

    def get_width(self) -> int:
        return self.label.get_width()

    def get_height(self) -> int:
        return self.label.get_height()

    def get_size(self) -> tuple[int, int]:
        return self.label.get_width(), self.label.get_height()

    def get_center_x(self) -> int:
        return (self.surface_width - self.label.get_width()) / 2

    def get_center_y(self) -> int:
        return (self.surface_height - self.label.get_height()) / 2

    def get_center_both(self) -> tuple[int, int]:
        return self.get_center_x(), self.get_center_y()

    def _1decimal_to_pixels_width(self, coord: int or float) -> int or float:
        return coord * self.surface_width

    def _1decimal_to_pixels_height(self, coord: int or float) -> int or float:
        return coord * self.surface_height

    def _2decimals_to_pixels(self, coord_width: int or float, coord_height: int or float) -> int or float:
        return self._1decimal_to_pixels_width(coord_width), self._1decimal_to_pixels_height(coord_height)

    def blit(self, x: int, y: int):
        self.blitted = True
        self.x = x
        self.y = y
        self.surface.blit(self.label, (self.x, self.y))
