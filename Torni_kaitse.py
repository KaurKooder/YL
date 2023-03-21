import pygame as pg

def main():
    pg.init()
    pg.display.set_caption("mäng")
    screen = pg.display.set_mode((1200, 600))
    player = pg.image.load("capu.png").convert_alpha()

    #objektid


    running = True

    x = 0
    y = 0
    xT = 1000
    yT = 550
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        #pg.time.delay(10)

        #if xKoordinaat == 800:
          #  xKoordinaat=1100
        #xKoordinaat-=1
        #screen.fill((0,0,0))

        if xT == 200:
            xT = 1100



        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                x += 10
            if event.key == pg.K_LEFT:
                 x -= 10
            if event.key == pg.K_DOWN:
                y += 10
            if event.key == pg.K_UP:
                y -= 10

        xT -= 0.1

        #screen.blit(player, (x, y))
        screen.fill("white")
        pg.draw.rect(screen, (255, 0, 0), (xT, yT, 50, 50))# teises sulus on ristküliku asukoht ja mõõtmed ekraanil
        pg.draw.rect(screen, (100, 100, 100), (0, 100, 200, 600))
        pg.display.update()



main()
