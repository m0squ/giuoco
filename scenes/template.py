# External modules #
import pygame

# Internal modules #
from utils.errors import SceneDrawNotOverridden
from interface.button import Button
from interface.label_back import LabelBack


class Scene:
    def __init__(self, display, change_scene, previous_scene: None or object = None):
        self.display = display
        self.change_scene = change_scene
        self.previous_scene = previous_scene
        self.display_size = self.display.get_size()
        self.display_width, self.display_height = self.display_size
        self.scene_just_changed = True
        self.buttons = []
        if self.previous_scene:
            self.back_label = LabelBack(self.display)

    """ Override this method in your child class before calling blit() """
    def draw(self):
        raise SceneDrawNotOverridden("override draw() in your child class before calling blit()")

    def blit(self):
        self.draw()
        if self.previous_scene:
            self.back_label.blit_to_default_position()
            self.add_button(Button(self.back_label, on_click=lambda: self.change_scene(self.previous_scene)))
        if self.scene_just_changed:
            self.scene_just_changed = False

    def add_button(self, button: Button):
        if self.scene_just_changed:
            self.buttons.append(button)

    def check_keypresses(self, event: pygame.event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if self.previous_scene:
                    self.change_scene(self.previous_scene)

    def check_button_clicks(self, event: pygame.event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                button.check_is_clicked()

    def check_events(self, event: pygame.event):
        self.check_keypresses(event)
        self.check_button_clicks(event)
