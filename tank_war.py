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
        self.rect.bottom=HEIGHT-10
        self.speed=8
        self.direccion="UP"
    def update(self) -> None:
        key_pressed =pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x+=self.speed
            self.image=self.tank.subsurface((66,0),(34,34))
            self.direccion="RIGHT"
        if key_pressed[pygame.K_LEFT]:
            self.rect.x-=self.speed
            self.image=self.tank.subsurface((200,0),(34,34))
            self.direccion="LEFT"
        if key_pressed[pygame.K_UP]:
            self.rect.y-=self.speed
            self.image=self.tank.subsurface((0,0),(34,34))
            self.direccion="UP"
        if key_pressed[pygame.K_DOWN]:
            self.rect.y+=self.speed
            self.image=self.tank.subsurface((135,0),(34,34))
            self.direccion="DOWN"
        if(self.rect.right>WIDTH):
            self.rect.right=WIDTH
        if(self.rect.left<0):
            self.rect.left=0
        if(self.rect.top<0):
            self.rect.top=0
        if(self.rect.bottom>HEIGHT):
            self.rect.bottom=HEIGHT
    def shoot(self):
        bullet=Bullet(self.rect.centerx,self.rect.centery,self.direccion)
        all_sprites.add(bullet)
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direccion) -> None:
        super().__init__()
        self.bullets=['./pic/bullet.png','./pic/bullet1.png','./pic/bullet2.png','./pic/bullet3.png']
        self.direccion=direccion
        if self.direccion=="UP":
            self.bullet=pygame.image.load(self.bullets[0])
        if self.direccion=="DOWN":
            self.bullet=pygame.image.load(self.bullets[2])
        if self.direccion=="LEFT":
            self.bullet=pygame.image.load(self.bullets[3])
        if self.direccion=="RIGHT":
            self.bullet=pygame.image.load(self.bullets[1])
        self.image=self.bullet
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()
        self.rect.x=x-15
        self.rect.y=y-15
        self.speed=10
    def update(self):
        if self.direccion=="UP":
            self.rect.y-=self.speed
        if self.direccion=="DOWN":
            self.rect.y+=self.speed
        if self.direccion=="LEFT":
            self.rect.x-=self.speed
        if self.direccion=="RIGHT":
            self.rect.x+=self.speed
        if self.rect.bottom>HEIGHT:
            self.kill()
        if self.rect.left<0:
            self.kill()
        if self.rect.right>WIDTH:
            self.kill()
        if self.rect.top<0:
            self.kill()

all_sprites=pygame.sprite.Group()
player=Player()
all_sprites.add(player)
while runing:
    clock.tick(FPS)
    for even in pygame.event.get():
        if even.type==pygame.QUIT:
            runing=False
        elif even.type==pygame.KEYDOWN:
            if(even.key ==pygame.K_SPACE):
                player.shoot()
    screen.fill(BLACK)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()
