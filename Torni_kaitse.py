import pygame as pg

def main():
    pg.init()
    pg.display.set_caption("mäng")
    screen = pg.display.set_mode((1200, 600))

    bg = pg.image.load("bg1.jpg")
    bg = pg.transform.scale(bg, (1200, 600))

    player = pg.image.load("kalash.png").convert_alpha()
    player = pg.transform.scale(player, (100, 50))


    bot = pg.image.load("capu2.png").convert_alpha()
    bot = pg.transform.scale(bot, (50, 50))

    running = True

    x = 0
    y = 0
    xT = 1000
    yT = 550

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        rect = player.get_rect(center=(320, 240))
        if xT <= 200:
            xT = 1100

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                x += 1
            if event.key == pg.K_LEFT:
                x -= 1
            if event.key == pg.K_DOWN:
                y += 1
            if event.key == pg.K_UP:
                player= pg.transform.rotate(player, 1)



        xT -= 0.1

        screen.blit(bg, (0, 0))
        pg.draw.rect(screen, (0, 255, 0), (xT, yT-20, 50, 10))# teises sulus on ristküliku asukoht ja mõõtmed ekraanil
        pg.draw.rect(screen, (100, 100, 100), (0, 100, 200, 600))

        screen.blit(player, (x, y))
        screen.blit(bot, (xT, yT))
        pg.display.update()



main()
