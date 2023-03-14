import pygame as pg

def main():
    pg.init()
    screen = pg.display.set_mode((1200, 600))
    screen.fill((0, 0, 0))
    player = pg.image.load("pilt\capu.png").convert_alpha()

    running=True
    x=0
    y=0

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    x += 10
                if event.key == pg.K_LEFT:
                    x -= 10
                if event.key == pg.K_DOWN:
                    y += 10
                if event.key == pg.K_UP:
                    y -= 10

        screen.fill((0, 0, 0))
        screen.blit(player, (x, y))

        pg.display.update()

main()