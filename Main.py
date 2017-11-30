import pygame       #for game like moves,sound etc.
import sys          #exit function to exit out of the program
import random       #random module for random placing items
import time         #that is obvious

print(pygame.init()); #left number succesfull tasks completed, right number errors
check_errors = pygame.init();

if check_errors[1] > 0:
    print("errors found, quiting...");
    sys.exit(-1); #-1 value is standard
else :
    print("PyGame succesfully initialized!")

# Play surface
playSurface = pygame.display.set_mode((720, 460));    #set height and width of window, set_mode expects values as tuple
pygame.display.set_caption('Snake v0.1');             #set title for window

# Colors
red = pygame.Color(255,0,0)         #game over
green = pygame.Color(0,255,0)       #snake
black = pygame.Color(0,0,0)         #score
white = pygame.Color(255,255,255)   #background
brown = pygame.Color(165,42,42)     #food

#Frames per second
fpsController = pygame.time.Clock()

#Variables
snakePos = [100, 50]
snakeBody = [[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]     #x,y cooridnates, position of snake is chaning by 10 so foodPos has to be divisible by ten
foodSpawn = True

direction = 'RIGHT'
changeTo = direction

score = 0

# Game Over function

def gameOver():
    myFont = pygame.font.SysFont('monaco',72)                   #font from system
    surfaceGameOver = myFont.render('Game Over!',True,red)      #second argument: alliased or anti-alliased
    GOrect = surfaceGameOver.get_rect()                         #Game Over in rectangle
    GOrect.midtop= (360,140)                         #Height and witdth / 2
    playSurface.blit(surfaceGameOver,GOrect)
    pygame.display.flip()
    showScore(0)
    time.sleep(4)                           # keep on the screen
    pygame.quit()       #for window
    sys.exit()          #for console

def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 24)
    sSurf = sFont.render('Score: {0}'.format(score), True, red)
    sRect = sSurf.get_rect()
    if choice == 1:
        sRect.midtop = (80, 10)
    else:
        sRect.midtop = (360, 120)
    playSurface.blit(sSurf,sRect)
    pygame.display.flip()

# Main logic
while 1:                    #1 - True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):             # ord of key - number value
                changeTo = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeTo = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeTo = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeTo = 'DOWN'


#v validation of direction

    if changeTo == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeTo == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeTo == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
# Snake position
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

# Snake body mechanism
    snakeBody.insert(0,list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()                                         # pop remove item from the list

    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn = True

    playSurface.fill(white)                                     #white background

# Draw Snake

    for pos in snakeBody:

        pygame.draw.rect(playSurface,green,                                     #drawing snake from rectangles
        pygame.Rect(pos[0], pos[1], 10, 10))                     # x,y, xsize,ysize

 # Draw food

    pygame.draw.rect(playSurface, brown,
    pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] <0 :
        gameOver()

    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()


    pygame.display.update()                                      #update settings
    showScore()
    fpsController.tick(20)                                               #frames per second

