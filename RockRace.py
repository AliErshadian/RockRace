import pygame
import time
import random

pygame.init()
pygame.mixer.init()


display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

car_width = 40
car_height = 84


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racing')
clock = pygame.time.Clock()


carImg = pygame.image.load('racecar.png')
bg = pygame.image.load('BG.jpg')
rock = pygame.image.load('rock.png')

pygame.mixer.music.load('shift.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.5)

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, yellow)
    gameDisplay.blit(text, (0,0))

def things(thingx , thingy, thingw, thingh):
 #   pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    gameDisplay.blit(pygame.transform.scale(rock, (thingw, thingh)), (thingx, thingy))

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, green)
    return textSurface, textSurface.get_rect()
    

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 45)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit (TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(3)

    game_loop()

def crash(score):
    text = 'You Crashed, you score is:' + str(score)

    s = pygame.mixer.Sound('crash.wav')
    s.play()

    message_display(text)
    
    


    

def game_loop():

    
    
    x = (display_width * 0.45)
    y = (display_height * 0.6)

    x_change = 0
    y_change = 0

    thing_width = 100
    thing_height = 100
    thing_startx = random.randrange(75, (display_width -75))
    #
    if (thing_startx + thing_width) > (display_width - 75):
        thing_startx -= (thing_startx + thing_width) - (display_width - 75)
    #
    thing_starty = -600
    thing_speed = 10

    dodged = 0
    
    bgy = -599

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10
                if event.key == pygame.K_UP:
                    y_change = -10
                if event.key == pygame.K_DOWN:
                    y_change = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

             

        x += x_change
        y += y_change
        
        gameDisplay.blit(bg, (0,bgy))
        if bgy < 0:
            bgy += thing_speed
        else:
            bgy = -599
            
        #things(thingx , thingy, thingw, thingh)
        things(thing_startx, thing_starty, thing_width, thing_height)
        thing_starty += thing_speed
        
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0 or y > display_height - car_height or y < 0:
            crash(dodged)

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(75.0, (display_width -75))
            if (thing_startx + thing_width) > (display_width - 75):
                thing_startx -= (thing_startx + thing_width) - (display_width - 75)

            dodged += 1
            thing_speed += 1
            if (dodged % 2) == 0:
                thing_width += (dodged * 2)
                thing_height += (dodged * 2)
            
            
        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width: 
                crash(dodged)
            
        pygame.display.update()
        clock.tick(60)






game_loop()
pygame.quit()
quit()
