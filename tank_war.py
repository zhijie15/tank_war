import pygame
import os
FPS=30
WIDTH=1550
HEIGHT=780
WHITE=(255,255,255)
BLACK=(0,0,0)
pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("坦克大战")
clock=pygame.time.Clock()
runing=True
class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        tank_img=pygame.image.load(os.path.join("pic","tank_sprite.png")).convert()
        self.tank=tank_img
        self.tank.set_colorkey(WHITE)
        self.image=self.tank.subsurface((0,0),(34,34))
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH/2
        self.rect.bottom=HEIGHT
        self.speed=8
    def update(self) -> None:
        key_pressed =pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x+=self.speed
            self.image=self.tank.subsurface((66,0),(34,34))
        if key_pressed[pygame.K_LEFT]:
            self.rect.x-=self.speed
            self.image=self.tank.subsurface((200,0),(34,34))
        if key_pressed[pygame.K_UP]:
            self.rect.y-=self.speed
            self.image=self.tank.subsurface((0,0),(34,34))
        if key_pressed[pygame.K_DOWN]:
            self.rect.y+=self.speed
            self.image=self.tank.subsurface((135,0),(34,34))
        if(self.rect.right>WIDTH):
            self.rect.right=WIDTH
        if(self.rect.left<0):
            self.rect.left=0
        if(self.rect.top<0):
            self.rect.top=0
        if(self.rect.bottom>HEIGHT):
            self.rect.bottom=HEIGHT
all_sprites=pygame.sprite.Group()
player=Player()
all_sprites.add(player)
while runing:
    clock.tick(FPS)
    for even in pygame.event.get():
        if even.type==pygame.QUIT:
            runing=False
    screen.fill(BLACK)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()
