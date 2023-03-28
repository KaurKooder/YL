import pygame as pg

def main():
    pg.init()
    screen = pg.display.set_caption("mäng")
    screen = pg.display.set_mode((1200, 600))
    color=(255,0,0)
    xKoordinaat = 1
    pg.draw.rect(screen, color, pg.Rect(xKoordinaat,30,60,60))  # teises sulus on ristküliku asukoht ja mõõtmed ekraanil
    player = pg.image.load("capu.png").convert_alpha()

    running = True

    x = 0
    y = 0
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        pg.time.delay(10)
        #if xKoordinaat == 400:
        #    xKoordinaat=0
        #xKoordinaat+=1
       # screen.fill((0,0,0))

        if xKoordinaat == 700:
            xKoordinaat = 0
        pg.time.delay(10)
        screen.fill((0,0,0))
        pg.draw.rect(screen, (255, 0, 0), (xKoordinaat, 30, 60, 60))# teises sulus on ristküliku asukoht ja mõõtmed ekraanil
        xKoordinaat += 1



        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                x += 10
            if event.key == pg.K_LEFT:
                 x -= 10
            if event.key == pg.K_DOWN:
                y += 10
            if event.key == pg.K_UP:
                y -= 10

        screen.blit(player, (x, y))

        pg.display.update()


main()
