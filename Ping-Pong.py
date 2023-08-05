from pygame import *
from random import *
from time import time as timer
game = True
FPS = 60
clock = time.Clock()
win_height = 500
window = display.set_mode((700, 500))
display.set_caption("ping pong")
bg = window.fill((200, 255, 255))
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class PlayerClass(GameSprite):
    def updateL(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    def updateR(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

racket1 = PlayerClass('racket.png', 30, 200, 50, 150, 4)
racket2 = PlayerClass('racket.png', 520, 200, 50, 150, 4)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill((200, 255, 255))
        racket1.updateL()
        racket2.updateR()

        racket1.reset()
        racket2.reset()

    display.update()
    clock.tick(FPS)
