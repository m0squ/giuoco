# External modules #
import pygame

# Internal modules #
from utils.errors import ButtonOnClickIsNoneError, LabelNotBlittedError
from interface.label import Label

button_left = 0
button_middle = 1
button_right = 2


class Button:
    def __init__(self, label: Label, on_click=None):
        self.label = label
        if not self.label.blitted:
            raise LabelNotBlittedError("call Label.blit function before assigning a Button to the Label")
        self.on_click = on_click
        self.x = self.label.x
        self.y = self.label.y
        self.rect = pygame.Rect(self.x, self.y, self.label.get_width(), self.label.get_height())

    def check_is_clicked(self, button: int = button_left):
        if self.on_click:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[button]:
                if self.rect.collidepoint(mouse_x, mouse_y):
                    self.on_click()
        else:
            raise ButtonOnClickIsNoneError("specify the on_click parameter when calling the constructor")
