from utils import settings
from utils.settings import write_setting
from interface.fonts import title_font, header_font
from interface.label import Label
from interface.button import Button
import scenes.home
import scenes.template


def get_fps_label_content() -> str:
    fps_label_content = "FPS: "
    fps_label_content += str(settings.fps) if settings.fps else "UNLIMITED"
    return fps_label_content


class SettingsScene(scenes.template.Scene):
    def __init__(self, display, change_scene):
        super().__init__(display, change_scene, previous_scene=scenes.home.HomeScene)
        self.settings_title_label = Label(self.display, "Settings", title_font)
        self.fps_label = Label(self.display, get_fps_label_content(), header_font)  # self.get_fps_label_content()

    def change_fps(self):
        settings.fps = settings.fps + 20 if settings.fps < 200 else 0
        self.fps_label.set_content(get_fps_label_content())
        write_setting("fps", settings.fps)

    def draw(self):
        self.settings_title_label.blit(self.settings_title_label.get_center_x(),
                                       self.settings_title_label._1decimal_to_pixels_height(.2))
        self.fps_label.blit(*self.fps_label.get_center_both())
        self.add_button(Button(self.fps_label, on_click=self.change_fps))
