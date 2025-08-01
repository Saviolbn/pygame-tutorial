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

def draw_task(color,y_coord):
    # draw on screen with a color, at these positions, with these sizes
    # a circle hollow inside, 5 line size
    pygame.draw.circle(screen, color,(30,y_coord),20,5)
    # a rectangle, relative to the position of the circle
    pygame.draw.rect(screen, color,[70, y_coord-15,200,30])
    # a black rectangle on top of the last one, -10 height and width so the line is size 5
    pygame.draw.rect(screen, black,[75, y_coord-10,190,20])


running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            
    screen.fill(background)
    draw_task(green,50)
    draw_task(blue,100)
    draw_task(red,150)
    pygame.display.flip()
    
    
pygame.quit()
            