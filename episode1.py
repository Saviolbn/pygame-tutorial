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
# game vars
green_value = 1
red_value = 2
orange_value = 3
white_value = 4
purple_value = 5


def draw_task(color,y_coord,value):
    # draw on screen with a color, at these positions, with these sizes
    # a circle hollow inside, 5 line size
    pygame.draw.circle(screen, color,(30,y_coord),20,5)
    # a rectangle, relative to the position of the circle
    pygame.draw.rect(screen, color,[70, y_coord-15,200,30])
    # a black rectangle on top of the last one, -10 height and width so the line is size 5
    pygame.draw.rect(screen, black,[75, y_coord-10,190,20])
    
    #initialize text
    value_text = font.render(str(value),True,white)
    #render text
    screen.blit(value_text,(16,y_coord- 10))

running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            
    screen.fill(background)
    # task is button and progress bar
    draw_task(green,50,green_value)
    draw_task(red,110,red_value)
    draw_task(orange,170,orange_value)
    draw_task(white,230,white_value)
    draw_task(purple,290,purple_value)
    pygame.display.flip()
    
    
pygame.quit()
            