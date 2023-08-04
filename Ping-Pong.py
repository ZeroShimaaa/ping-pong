from pygame import *
from random import *
from time import time as timer
game = True
FPS = 60
clock = time.Clock()
window = display.set_mode((700, 500))
display.set_caption("ping pong")
bg = window.fill(((200, 255, 255)))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

class PlayerClass(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if key_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
