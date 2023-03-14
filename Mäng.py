import pygame as pg

def main():
    pg.init()
    screen = pg.display.caption("mäng")
    screen = pg.display.set_mode((1200, 600))
    color=(255,0,0)
    xKoordinaat = 1
    pg.draw.rect(screen, color, pg.Rect(xKoordinaat,30,60,60))  # teises sulus on ristküliku asukoht ja mõõtmed ekraanil
    pg.display.update()

running = True

class ruut:
    def __init__(self, kyljePikkus):
        self.kyljePikkus = kyljePikkus

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.time.delay(10)
    if x == 400:
        x=0
    x+=1
    screen.fill((0,0,0))
            break

    if xKoordinaat == 700:
        xKoordinaat = 0
    pg.time.delay(10)
    screen.fill((0,0,0))
    pg.draw.rect(screen, (255, 0, 0), (xKoordinaat, 30, 60, 60))# teises sulus on ristküliku asukoht ja mõõtmed ekraanil

    xKoordinaat += 1
    pg.display.update()