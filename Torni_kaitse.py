import pygame as pg

def rotate(image, rect, angle):
    new_image = pg.transform.rotate(image, angle)
    rect = new_image.get_rect(center=rect.center)
    return new_image, rect
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

    x = 100
    y = 200
    xT = 1000
    yT = 550

    #blue = pg.Color('dodgerblue2')

    #image = pg.Surface((320, 200), pg.SRCALPHA)
    #image = player
    #pg.draw.polygon(image, blue, ((0, 0), (320, 100), (0, 200)))
    # Keep a reference to the original to preserve the image quality.
    orig_image = player
    rect = player.get_rect(center=(100, 150))
    angle = 0


    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.blit(bg, (0, 0))
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                x += 1
            if event.key == pg.K_LEFT:
                x -= 1
            if event.key == pg.K_DOWN:
                angle -= 0.1
                player, rect = rotate(orig_image, rect, angle)
            if event.key == pg.K_UP:
                angle += 0.1
                player, rect = rotate(orig_image, rect, angle)
                #screen.blit(player, rect)
                #pg.display.flip()

        if xT <= 200:
            xT = 1000
        xT -= 0.1



        #torn
        pg.draw.rect(screen, (100, 100, 100), (0, 100, 200, 600))
        # health bar
        pg.draw.rect(screen, (0, 255, 0), (xT, yT - 20, 50, 10))  # teises sulus on ristküliku asukoht ja mõõtmed ekraanil

        screen.blit(player, (x, y))
        screen.blit(bot, (xT, yT))

        pg.display.update()




main()
