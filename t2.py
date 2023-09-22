import pygame
import random
import sys

pygame.init() #initialises 

screen_width=800
screen_height=300

score=0
player_lives=3
font = pygame.font.Font(None,36)
game_over_font=pygame.font.Font(None,64)

bg_x=0

running=True
clock = pygame.time.Clock()

speed_increase_rate=0

background_image=pygame.image.load("assets/VulcanBack.png")
background_image=pygame.transform.scale(background_image ,(screen_width,screen_height))
screen=pygame.display.set_mode((screen_width , screen_height)) #variable for screen
pygame.display.set_caption("Drago planets")


class Character:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img = pygame.image.load("assets/dragon1.png")
        self.img = pygame.transform.scale(self.img , (100,100))
        self.rect = self.img.get_rect()
        self.rect.center = (x,y)
        self.run_animation_count = 0
        self.img_list= ["assets/dragon1.png","assets/dragon2.png","assets/dragon3.png"]

    # def draw(self):
    #     self.rect.center = (self.x , self.y)
    #     screen.blit(self.img , self.rect)
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    bg_x -= (10+speed_increase_rate)
    speed_increase_rate+=0.006
    if bg_x<=-screen_width:
        bg_x=0
    screen.blit(background_image,(bg_x,0))
    screen.blit(background_image,(screen_width+bg_x,0))
    pygame.display.update()
    clock.tick(30)

pygame.quit()