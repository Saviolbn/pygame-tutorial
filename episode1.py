import pygame
pygame.init()

# color library
red = (225,0,0)
green = (0,255,0)
blue = (0,0,225)
white = (225,225,225)
black = (0,0,0)
purple = (127,0,225)
orange = (225,165,0)

screen = pygame.display.set_mode([300,450])
pygame.display.set_caption('idlegame mostbasic, @LeMaster Tech')
background = black
framerate = 60
font = pygame.font.Font('freesansbold.ttf',16)
timer = pygame.time.Clock()

running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            
    screen.fill(background)
    pygame.display.flip()
    
    
pygame.quit()
            