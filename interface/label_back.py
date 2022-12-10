from interface.fonts import header_font
from interface.label import Label


class LabelBack(Label):
    def __init__(self, display):
        super().__init__(display, "< Back", header_font)

    def blit_to_default_position(self):
        self.blit(*self._2decimals_to_pixels(.1, .1))
