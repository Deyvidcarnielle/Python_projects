import pygame
from menu import Menu, GameOver
from game import Game

class Main:

    def __init__(self, sizex, sizey, title):

        pygame.init()

        pygame.mixer.init()
        pygame.mixer.music.load("assets_TR/lofi.wav")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.loop = True
        self.fps = pygame.time.Clock()

        self.start_screen = Menu("assets_TR/pixil-space.png")
        self.game = Game()
        self.gameover = GameOver("assets_TR/pixil-gameover.png")
        self.victory = GameOver("assets_TR/VICTORY.png")

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
            if not self.start_screen.change_scene:
                self.start_screen.event(event)
            elif not self.game.game_loss and not self.game.game_win:
                self.game.trash.move_trash(event)
            elif self.game.game_loss:
                self.gameover.event(event)
            elif self.game.game_win:
                self.victory.event(event)

    def draw(self):

        if not self.start_screen.change_scene:
            self.start_screen.draw(self.window)
        elif not self.game.game_loss and not self.game.game_win:
            self.game.draw(self.window)
            self.game.update()
        elif not self.gameover.change_scene and self.game.game_loss:
            self.gameover.draw(self.window)
        elif not self.victory.change_scene and self.game.game_win:
            self.victory.draw(self.window)
        else:
            self.start_screen.change_scene = False
            self.game.game_win = False
            self.game.game_loss = False
            self.gameover.change_scene = False
            self.victory.change_scene = False

            self.game.trash.life = 3
            self.game.trash.pts = 0

    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.events()
            pygame.display.update()

game = Main(360, 640, "Trash Rocket")
game.update()
