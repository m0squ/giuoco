# External modules #
import easygui
import pygame

pygame.init()

# Internal modules #
from utils import settings
from scenes.home import HomeScene, get_running, set_running


def kill():
    set_running(False)
    pygame.mixer.music.stop()
    pygame.quit()


def kill_and_quit(code=0):
    kill()
    quit(code)


class Videogame:
    def __init__(self):
        # Application #
        pygame.init()
        self.display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.display_size = self.display.get_size()
        self.display_width, self.display_height = self.display_size
        pygame.display.set_caption("Giuoco enea")
        # pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()
        # Images #
        self.home_bg = pygame.transform.scale(pygame.image.load("img/home_bg.jpg"), self.display_size)
        # Audio #
        pygame.mixer.init()
        pygame.mixer.music.load("audio/home.ogg")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)  # Make the music repeat infinitely
        # Interface #
        self.scene = HomeScene(self.display, self.change_scene)

    def change_scene(self, scene):
        self.scene = scene(self.display, self.change_scene)

    def catch_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not self.scene.previous_scene:
                        set_running(False)
            elif event.type == pygame.QUIT:
                set_running(False)
            self.scene.check_events(event)

    def draw(self):
        self.display.blit(self.home_bg, (0, 0))
        self.scene.blit()

    def update(self):
        pygame.display.update()
        self.clock.tick(settings.fps)  # Use 0 to get max FPS

    def main(self):
        while get_running():
            self.catch_events()
            self.draw()
            self.update()
        kill_and_quit()


if __name__ == "__main__":
    try:
        Videogame().main()
    except KeyboardInterrupt:
        print("^C")
        kill_and_quit(code=1)
    except Exception as e:
        kill()
        print(str(type(e).__name__) + ":", e)
        easygui.exceptionbox("DIOCANEEEEE nonostante tre ore di debugging", "Fatal error")
        quit(1)
