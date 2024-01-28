import pygame
FPS=30
WIDTH=500
HEIGHT=600
WHITE=(255,255,255)
GREEN=(0,255,0)
pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
clock=pygame.time.Clock()
runing=True
class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image=pygame.Surface((50,50))
        self.image.fill(GREEN)
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH/2
        self.rect.bottom=HEIGHT-10
        self.speed=8
    def update(self) -> None:
        key_pressed =pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x+=self.speed
        if key_pressed[pygame.K_LEFT]:
            self.rect.x-=self.speed
        if key_pressed[pygame.K_UP]:
            self.rect.y-=self.speed
        if key_pressed[pygame.K_DOWN]:
            self.rect.y+=self.speed
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
    screen.fill(WHITE)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()
