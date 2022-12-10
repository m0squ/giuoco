from interface import fonts
from interface.label import Label
from interface.button import Button
import scenes.settings
import scenes.template

running = True


def get_running() -> bool:
    return running


def set_running(value: bool):
    global running
    running = value


class HomeScene(scenes.template.Scene):
    def __init__(self, display, change_scene):
        super().__init__(display, change_scene)
        self.title = Label(self.display, "Home", fonts.title_font)
        self.settings_label = Label(self.display, "Settings", fonts.header_font)
        self.quit_label = Label(self.display, "Quit game", fonts.header_font)

    def draw(self):
        self.title.blit(self.title.get_center_x(), self.title._1decimal_to_pixels_height(.2))
        self.settings_label.blit(self.settings_label.get_center_x(),
                                 self.settings_label._1decimal_to_pixels_height(.43))
        self.quit_label.blit(self.quit_label.get_center_x(), self.quit_label._1decimal_to_pixels_height(.53))
        self.add_button(Button(self.settings_label, on_click=lambda: self.change_scene(scenes.settings.SettingsScene)))
        self.add_button(Button(self.quit_label, on_click=lambda: set_running(False)))
