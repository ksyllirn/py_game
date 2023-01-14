from pygame import *
from time import sleep

window = display.set_mode((700,500))
display.set_caption("catch-up")
background = transform.scale(image.load("back.jpg"), (700,500))

sprite_1 = transform.scale(image.load("steve_1.png"), (110,150))
sprite_2 = transform.scale(image.load("creep.png"), (70,150))

bomb = transform.scale(image.load("bomb.png"), (150,150))

game = True

clock = time.Clock()
FPS = 60
x1, y1 = 140 , 240
x2, y2 = 500, 210

while game:
    window.blit(background, (0,0))
    window.blit(sprite_1, (x1,y1))
    window.blit(sprite_2, (x2,y2))

    keys_pressed = key.get_pressed()

    if keys_pressed[K_UP] and y2 >= 30:
        y2-=10

    if keys_pressed[K_DOWN] and y2 <= 340:
        y2+=10

    if keys_pressed[K_LEFT] and x2 >= 50:
        x2-=10

    if keys_pressed[K_RIGHT] and x2 <= 585:
        x2+=10

    if keys_pressed[K_w] and y1 >= 30:
        y1-=10

    if keys_pressed[K_s] and y1 <= 340:
        y1+=10

    if keys_pressed[K_a] and x1 >= 50:
        x1-=10

    if keys_pressed[K_d] and x1 <=585:
        x1+=10 

    
    if x2-x1<=20:
        window.blit(bomb, (x1, y1))
        display.update()
        sleep(1)
        game = False

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
