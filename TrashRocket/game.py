from obj import Obj, Trash, Text
import random


class Game:

    def __init__(self):

        self.bg = Obj("assets_TR/pixil-glass2.png", 0, 0)
        self.bg2 = Obj("assets_TR/pixil-glass2.png", 0, -640)

        self.pomba = Obj("assets_TR/pomba1.png", random.randrange(0, 300), -50)
        self.engr = Obj("assets_TR/engr1.png", random.randrange(0, 300), 200)
        self.trash = Trash("assets_TR/trash1.png", 150, 600)

        self.game_win = False
        self.game_loss = False

        self.score = Text(100, "0")
        self.lifes = Text(60, "3")

    def draw(self, window):
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.trash.drawing(window)
        self.pomba.drawing(window)
        self.engr.drawing(window)
        self.score.draw(window, 160, 50)
        self.lifes.draw(window, 50, 50)


    def update(self):
        self.move_bg()
        self.pomba.anim("pomba", 7, 3)
        self.engr.anim("engr", 4, 3)
        self.trash.anim("trash", 2, 5)
        self.move_pomba()
        self.move_engr()
        self.trash.colision(self.pomba.group, "pomba")
        self.trash.colision(self.engr.group, "engr")
        self.gameover()
        self.victory()

        self.score.update_text(str(self.trash.pts))
        self.lifes.update_text(str(self.trash.life))

    def move_bg(self):
        self.bg.sprite.rect[1] += 5
        self.bg2.sprite.rect[1] += 5

        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0

        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640

    def move_pomba(self):
        self.pomba.sprite.rect[1] += 15

        if self.pomba.sprite.rect[1] > 640:
            self.pomba.sprite.kill()
            self.pomba = Obj("assets_TR/pomba1.png", random.randrange(0, 320), -50)

    def move_engr(self):
        self.engr.sprite.rect[1] += 5

        if self.engr.sprite.rect[1] > 640:
            self.engr.sprite.kill()
            self.engr = Obj("assets_TR/engr1.png", random.randrange(0, 320), -50)

    def gameover(self):
        if self.trash.life <= 0:
            self.game_loss = True

    def victory(self):
        if self.trash.pts >= 10:
            self.game_win = True





