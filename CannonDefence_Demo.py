import math
import pygame as pg
from pygame.math import Vector2
from random import *



pg.init()
display_width = 1500
display_height = 1000
screen = pg.display.set_mode((display_width, display_height))
FONT = pg.font.Font(None, 24)
FONT1 = pg.font.Font(None, 100)


#kahurid
# The cannon image and rect.
cannon_img = pg.Surface((60, 22), pg.SRCALPHA)
cannon_alus = pg.Surface((60, 60), pg.SRCALPHA)
pg.draw.rect(cannon_alus, pg.Color('gray'), [0, 0, 50, 50])
pg.draw.rect(cannon_img, pg.Color('grey19'), [0, 0, 35, 22])
pg.draw.rect(cannon_img, pg.Color('grey19'), [35, 6, 35, 10])
orig_cannon_img = cannon_img  # Store orig image to preserve quality.
cannon = cannon_img.get_rect(center=(750, 500))
#crossbow image and rect
crossbow_img = pg.Surface((60, 60), pg.SRCALPHA)
pg.draw.rect(crossbow_img, pg.Color('brown'), [0, 25, 60, 10])
pg.draw.rect(crossbow_img, pg.Color('lightsalmon4'), [40, 0, 10, 60])
orig_crossbow_img = crossbow_img
crossbow = crossbow_img.get_rect(center=(750, 500))
#Shotty
shotty_img = pg.Surface((60, 22), pg.SRCALPHA)
pg.draw.rect(shotty_img, pg.Color('lightsalmon4'), [0, 0, 35, 22])
pg.draw.rect(shotty_img, pg.Color('grey19'), [35, 0, 35, 10])
pg.draw.rect(shotty_img, pg.Color('grey19'), [35, 12, 35, 10])
orig_shotty_img = shotty_img
shotty = shotty_img.get_rect(center=(750, 500))
#automaat
automaat_img = pg.Surface((60, 22), pg.SRCALPHA)
pg.draw.rect(automaat_img, pg.Color('green'), [0, 0, 35, 22])
pg.draw.rect(automaat_img, pg.Color('grey19'), [35, 0, 35, 10])
pg.draw.rect(automaat_img, pg.Color('grey19'), [35, 12, 35, 10])
orig_automaat_img = automaat_img
automaat = automaat_img.get_rect(center=(750, 500))
#alus
cannon_alus_keskpunkt = cannon_alus.get_rect(center=(755, 505))
#kuulid
#kuul
BULLET_IMAGE = pg.Surface((20, 11), pg.SRCALPHA)
pg.draw.polygon(BULLET_IMAGE, pg.Color('gold'), [(0, 0), (20, 5), (0, 11)])
#nool
ARROW_IMAGE = pg.Surface((60, 10), pg.SRCALPHA)
pg.draw.rect(ARROW_IMAGE, pg.Color('brown'), (5, 4, 50, 3))
pg.draw.polygon(ARROW_IMAGE, pg.Color('white'), [(40,0), (60, 5), (40, 10)])
#haavel
HAAVEL_IMAGE = pg.Surface((30, 70), pg.SRCALPHA)
pg.draw.rect(HAAVEL_IMAGE, pg.Color('black'), (randint(0,30), randint(0,70), 2, 2))
pg.draw.rect(HAAVEL_IMAGE, pg.Color('black'), (randint(0,30), randint(0,70), 2, 2))
pg.draw.rect(HAAVEL_IMAGE, pg.Color('black'), (randint(0,30), randint(0,70), 2, 2))
pg.draw.rect(HAAVEL_IMAGE, pg.Color('black'), (randint(0,30), randint(0,70), 2, 2))
pg.draw.rect(HAAVEL_IMAGE, pg.Color('black'), (randint(0,30), randint(0,70), 2, 2))
pg.draw.rect(HAAVEL_IMAGE, pg.Color('black'), (randint(0,30), randint(0,70), 2, 2))
pg.draw.rect(HAAVEL_IMAGE, pg.Color('black'), (randint(0,30), randint(0,70), 2, 2))


ENEMY_IMAGE = pg.Surface((40, 40), pg.SRCALPHA)
ENEMY_IMAGE1 = pg.Surface((40, 40), pg.SRCALPHA)
#amblikud
#amblik 1
#jalad
pg.draw.rect(ENEMY_IMAGE, pg.Color('gray6'), (0, 0, 5, 40))
pg.draw.rect(ENEMY_IMAGE, pg.Color('gray6'), (10, 0, 5, 40))
pg.draw.rect(ENEMY_IMAGE, pg.Color('gray6'), (20, 0, 5, 40))
#keha
pg.draw.rect(ENEMY_IMAGE, pg.Color('gray6'), (0, 10, 25, 20))
#pea
pg.draw.rect(ENEMY_IMAGE, pg.Color('gray6'), (25, 5, 15, 30))
#silmad
pg.draw.rect(ENEMY_IMAGE, pg.Color('red'), (30, 10, 3, 3))
pg.draw.rect(ENEMY_IMAGE, pg.Color('red'), (30, 25, 3, 3))
#amblik2
#jalad
pg.draw.rect(ENEMY_IMAGE1, pg.Color('grey82'), (0, 0, 5, 40))
pg.draw.rect(ENEMY_IMAGE1, pg.Color('grey82'), (10, 0, 5, 40))
pg.draw.rect(ENEMY_IMAGE1, pg.Color('grey82'), (20, 0, 5, 40))
#keha
pg.draw.rect(ENEMY_IMAGE1, pg.Color('grey82'), (0, 10, 25, 20))
#pea
pg.draw.rect(ENEMY_IMAGE1, pg.Color('grey82'), (25, 5, 15, 30))
#silmad
pg.draw.rect(ENEMY_IMAGE1, pg.Color('purple4'), (30, 10, 3, 3))
pg.draw.rect(ENEMY_IMAGE1, pg.Color('purple4'), (30, 25, 3, 3))


global vastaseelud
class Enemy(pg.sprite.Sprite):
    def __init__(self, pos, angle, speed):
        super(Enemy, self).__init__()
        self.image = pg.transform.rotate(ENEMY_IMAGE, -angle)
        self.rect = self.image.get_rect(center=pos)
        # To apply an offset to the start position,
        # create another vector and rotate it as well.
        offset = Vector2(-2000, 0).rotate(angle)
        # Add the offset vector to the position vector.
        self.pos = Vector2(pos) + offset  # Center of the sprite.
        # Rotate the velocity vector (9, 0) by the angle.
        self.vastaseelud = 2
        self.speed = speed
        self.velocity = Vector2(speed, 0).rotate(angle)

    def elu(self):
        if self.vastaseelud == 0:
            Enemy.kill(self)

    def update(self):
        # Add velocity to pos to move the sprite.
        self.pos += self.velocity
        self.rect.center = self.pos

class Enemy1(pg.sprite.Sprite):
    def __init__(self, pos, angle, speed):
        super(Enemy1, self).__init__()
        self.image = pg.transform.rotate(ENEMY_IMAGE1, -angle)
        self.rect = self.image.get_rect(center=pos)
        offset = Vector2(-2500, 0).rotate(angle)
        self.pos = Vector2(pos) + offset
        self.speed = speed
        self.vastaseelud = 4
        self.velocity = Vector2(speed, 0).rotate(angle)

    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos

class Bullet(pg.sprite.Sprite):

    def __init__(self, pos, angle):
        super(Bullet, self).__init__()
        self.image = pg.transform.rotate(BULLET_IMAGE, -angle)
        self.rect = self.image.get_rect(center=pos)
        # To apply an offset to the start position,
        # create another vector and rotate it as well.
        offset = Vector2(40, 0).rotate(angle)
        # Add the offset vector to the position vector.
        self.pos = Vector2(pos) + offset  # Center of the sprite.
        # Rotate the velocity vector (9, 0) by the angle.
        self.velocity = Vector2(9, 0).rotate(angle)
        self.damage = 1

    def update(self):
        # Add velocity to pos to move the sprite.
        self.pos += self.velocity
        self.rect.center = self.pos

class Arrow(pg.sprite.Sprite):

    def __init__(self, pos, angle):
        super(Arrow, self).__init__()
        self.image = pg.transform.rotate(ARROW_IMAGE, -angle)
        self.rect = self.image.get_rect(center=pos)
        offset = Vector2(40, 0).rotate(angle)
        self.pos = Vector2(pos) + offset
        self.velocity = Vector2(9, 0).rotate(angle)
        self.damage = 0.5

    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos

class Haavel(pg.sprite.Sprite):

    def __init__(self, pos, angle):
        super(Haavel, self).__init__()
        self.image = pg.transform.rotate(HAAVEL_IMAGE, -angle)
        self.rect = self.image.get_rect(center=pos)
        offset = Vector2(40, 0).rotate(angle)
        self.pos = Vector2(pos) + offset
        self.velocity = Vector2(9, 0).rotate(angle)
        self.damage = 0.5

    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos

def text_objects(text, font):
    textSurface = font.render(text, True, 'black')
    return textSurface, textSurface.get_rect()

def menu():
    pg.display.set_caption('Menu')

    intro = True

    while intro:
        for event in pg.event.get():
            print(event)
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                intro = False

        screen.fill('slateblue1')
        largeText = pg.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Vajuta hiirele, et alustada", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        tekst = FONT1.render("Tapa nii palju ämblikke kui suudad", True, 'blue')
        tekst1 = FONT1.render("Vajuta r-i, et relva laadida", True, 'blue')
        tekst2 = FONT1.render("Vajuta b-d, et avada pood", True, 'blue')
        tekst3 = FONT1.render("Vajuta hiirele, et tulistada", True, 'blue')
        screen.blit(tekst, (10, 10))
        screen.blit(tekst1, (10, 100))
        screen.blit(tekst2, (10, 200))
        screen.blit(tekst3, (10, 300))

        screen.blit(TextSurf, TextRect)
        pg.display.update()

def mangusisene_menu():
    global ammu
    global raha
    global listiindeks
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    HOVER_COLOR = (50, 70, 90)
    # Don't define new font objects in your while loop (that's inefficient).
    FONT = pg.font.SysFont("Times New Norman", 60)
    # If the text surfaces and button rects don't change,
    # you can define them once outside of the while loop.
    text1 = FONT.render("semi auto cannon, 10$", True, WHITE)
    text2 = FONT.render("buck shot cannon, 20$", True, WHITE)
    text3 = FONT.render("FULLAUTO! cannon, 50$", True, WHITE)
    text4 = FONT.render("AMMU, 2$", True, WHITE)
    rect1 = pg.Rect(300, 300, 455, 80)
    rect2 = pg.Rect(300, 400, 455, 80)
    rect3 = pg.Rect(300, 500, 495, 80)
    rect4 = pg.Rect(300, 600, 205, 80)
    # The buttons consist of a text surface, a rect and a color.
    buttons = [
        [text1, rect1, BLACK],
        [text2, rect2, BLACK],
        [text3, rect3, BLACK],
        [text4, rect4, BLACK],
    ]


    jookseb = True
    while jookseb:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_b:
                    jookseb = False
            elif event.type == pg.MOUSEMOTION:
                for button in buttons:
                    # button[1] is the rect. Use its collidepoint method with
                    # the `event.pos` (mouse position) to detect collisions.
                    if button[1].collidepoint(event.pos):
                        # Set the button's color to the hover color.
                        button[2] = HOVER_COLOR
                    else:
                        # Otherwise reset the color to black.
                        button[2] = BLACK

            elif event.type == pg.MOUSEBUTTONDOWN:
                    if buttons[3][1].collidepoint(event.pos):
                        if raha > 2:
                            ammu += 40
                            raha -= 2
                    elif buttons[0][1].collidepoint(event.pos):
                        if raha > 10:
                            raha -= 10
                            listiindeks = 0
                            listiindeks += 1
                    elif buttons[1][1].collidepoint(event.pos):
                        if raha > 20:
                            listiindeks = 0
                            listiindeks += 2
                            raha -= 20
                    elif buttons[2][1].collidepoint(event.pos):
                        if raha > 50:
                            listiindeks = 0
                            listiindeks += 3
                            raha -= 50

            screen.fill((20, 50, 70))

        # Draw the buttons with their current colors at their rects.
        # You can unpack the button lists directly in the head of the loop.
            for text, rect, color in buttons:
                pg.draw.rect(screen, color, rect)
                screen.blit(text, rect)


            pg.display.flip()

def main():
    global ammu
    global ammu_salves
    global raha
    global vastaseidlastud
    global erinevad_kuulid
    global listiindeks

    relvastusl = [crossbow, cannon, shotty, automaat]
    relvastus_imgl = [crossbow_img, cannon_img, shotty_img, automaat_img]
    orig_relvastus_imgl = [crossbow_img, cannon_img, shotty_img, automaat_img]
    erinevad_kuulidl = [0, 1, 2, 3]
    listiindeks = 0
    max_ammu_salvesl = [1, 10, 10, 30]
    laseronl=[0, 1, 0, 1]

    vastaseidlastud = 0
    ammu_salves = 0
    elud = 5
    ammu = 200
    raha = 0
    klikkonall=False

    pg.display.set_caption('Hea mang')
    clock = pg.time.Clock()

    # Add bullets to this group.
    bullet_group = pg.sprite.Group()
    # Add enemies to this group
    enemy_group = pg.sprite.Group()

    spawnratemuutuja = 10
    spawnratemuutuja1 = 5
    playing = True
    while playing:
        spawnrate = randint(0, 1000)
        if spawnrate < spawnratemuutuja:
            enemy_group.add(Enemy(cannon.center, angle, 4))
        if vastaseidlastud >= 10 and spawnrate < spawnratemuutuja1:
            enemy_group.add(Enemy1(cannon.center, angle, 2))
        #siit loeb mangija inputi
        for event in pg.event.get():
            if event.type == pg.QUIT:
                playing = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_b:
                    mangusisene_menu()

                if event.key == pg.K_r and ammu_salves == 0:
                    if ammu >= max_ammu_salvesl[listiindeks]:
                        ammu_salves += max_ammu_salvesl[listiindeks]
                        ammu -= max_ammu_salvesl[listiindeks]
                    else:
                        ammu_salves += ammu
                        ammu = 0


            elif event.type == pg.MOUSEBUTTONDOWN:
                # Left button fires a bullet from cannon center with
                # current angle. Add the bullet to the bullet_group.
                if ammu_salves > 0:
                    if event.button == 1 and erinevad_kuulidl[listiindeks] == 0:
                        bullet_group.add(Arrow(relvastusl[listiindeks].center, angle))
                        ammu_salves -= 1
                    if event.button == 1 and erinevad_kuulidl[listiindeks] == 1:
                        bullet_group.add(Bullet(relvastusl[listiindeks].center, angle))
                        ammu_salves -= 1
                    if event.button == 1 and erinevad_kuulidl[listiindeks] == 2:
                        bullet_group.add(Haavel(relvastusl[listiindeks].center, angle))
                        ammu_salves -= 1
                    if event.button == 1 and erinevad_kuulidl[listiindeks] == 3:
                        klikkonall=True
            elif event.type == pg.MOUSEBUTTONUP:
                klikkonall = False
        if klikkonall == True and ammu_salves > 0:
            bullet_group.add(Bullet(relvastusl[listiindeks].center, angle))
            ammu_salves -= 1

            # et mang jookseks smoothilt peab kaugemale lainud kuulid ara deletema
        for bullet in bullet_group:
            if bullet.rect.center[1] > 1000 or bullet.rect.center[0] > 1500 or bullet.rect.center[0] < 0 or bullet.rect.center[1] < 0 :
                bullet.kill()
                #vastaste tapmine kuulidega
            for enemy in enemy_group:
                if enemy.rect.colliderect(bullet.rect):
                    bullet.kill()
                    enemy.vastaseelud -= 1
                    if enemy.vastaseelud == 0:
                        enemy.kill()
                        spawnratemuutuja += 0.1
                        spawnratemuutuja1 += 0
                        vastaseidlastud += 1
                        raha += 0.2

        bullet_group.update()
        # Find angle to target (mouse pos).
        enemy_group.update()

        x, y = Vector2(pg.mouse.get_pos()) - relvastusl[listiindeks].center
        angle = math.degrees(math.atan2(y, x))
        # Rotate the cannon image.
        relvastus_imgl[listiindeks] = pg.transform.rotate(orig_relvastus_imgl[listiindeks], -angle)
        relvastusl[listiindeks] = relvastus_imgl[listiindeks].get_rect(center=relvastusl[listiindeks].center)

        #vastase kokkuporge mangijaga
        for enemy in enemy_group:
            if cannon_alus_keskpunkt[0]-20 < enemy.rect.center[0] < cannon_alus_keskpunkt[0]+80 and cannon_alus_keskpunkt[1]-20 < enemy.rect.center[1] < cannon_alus_keskpunkt[1]+80:
                enemy.kill()
                elud -= 1
                if elud <= 0:
                    playing = False



        # Draw
        screen.fill(pg.Color('darkolivegreen3'))
        bullet_group.draw(screen)
        enemy_group.draw(screen)
        screen.blit(cannon_alus, cannon_alus_keskpunkt)
        screen.blit(relvastus_imgl[listiindeks], relvastusl[listiindeks])
        txt = FONT.render('elud {:.1f}'.format(elud), True, 'red')
        txt1 = FONT.render('kills {:.1f}'.format(vastaseidlastud), True, 'red')
        txt2 = FONT.render('raha {:.1f}'.format(raha), True, 'palegreen4')
        txt3 = FONT.render('ammu {:.1f}'.format(ammu), True, 'powderblue')
        txt4 = FONT.render('ammu_salves {:.1f}'.format(ammu_salves), True, 'powderblue')

        screen.blit(txt, (10, 10))
        screen.blit(txt1, (10, 30))
        screen.blit(txt2, (10, 50))
        screen.blit(txt3, (10, 70))
        screen.blit(txt4, (10, 90))
        if laseronl[listiindeks] == 1:
            pg.draw.line(
                screen, pg.Color(150, 60, 20),
                relvastusl[listiindeks].center, pg.mouse.get_pos(), 2)
        pg.display.update()

        clock.tick(60)

#if __name__ == '__main__':
menu()
main()
pg.quit()