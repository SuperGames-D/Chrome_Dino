import pygame
from pygame.locals import *
from pygame import mixer
import time
import keyboard
import random


def draw_block():
    # surface.fill((100, 110, 5))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()


def draw_spike():
    surface.blit(spike, (spike_x, spike_y))
    pygame.display.flip()


def draw_cloud():
    surface.blit(cloud, (cloud_x, cloud_y))
    pygame.display.flip()


pygame.init()

surface = pygame.display.set_mode((1250, 652))
surface.fill((248, 248, 255))
pygame.display.set_caption("Chrome Dino")


block = pygame.image.load("dino_walk1.png").convert()
block = pygame.transform.rotate(block, 0)
block_x = 200
block_y = 240
surface.blit(block, (block_x, block_y))
floor = pygame.image.load("dino_floor.png").convert()
surface.blit(floor, (0, 460))

spike = pygame.image.load("cactus.png").convert()
spike_x = 1300
spike_y = 375
surface.blit(spike, (spike_x, spike_y))

cloud = pygame.image.load("dino_cloud.png").convert()
cloud_x = 1000
cloud_y = 100
surface.blit(spike, (spike_x, spike_y))


pygame.display.flip()

mixer.init()

score = 0
high = 0
speed = 17

pygame.font.init()

my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render(str(score), False, (0, 0, 0))
surface.blit(floor, (-40, -270))
surface.blit(text_surface, (550, 0))
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render("HI" + str(high), False, (0, 0, 0))
surface.blit(text_surface, (650, 0))
level = 1

menu = True

running = True

while running:
    if not menu:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_SPACE:
                    music = mixer.Sound("dino_jump.wav")
                    music.play()
                    for x in range(1, 10):
                        block_y -= 12
                        spike_x -= speed
                        cloud_x -= speed / 4
                        draw_spike()
                        draw_block()
                        draw_cloud()
                        score += 0.5
                        surface.blit(floor, (-40, -270))
                        text_surface = my_font.render(str(round(score)), False, (0, 0, 0))
                        surface.blit(text_surface, (1000, 0))
                        my_font = pygame.font.SysFont('Comic Sans MS', 30)
                        text_surface = my_font.render("HI " + str(high), False, (0, 0, 0))
                        surface.blit(text_surface, (830, 0))
                        if (score / 100).is_integer():
                            music = mixer.Sound("dino_score.wav")
                            music.play()
                            speed = speed * 1.1
                        if (block_x + int("30")) >= spike_x >= (block_x - int("30")) and block_y >= int("450"):
                            if score >= high:
                                high = round(score)
                                surface.blit(floor, (-40, -270))
                                text_surface = my_font.render(str(round(score)), False, (0, 0, 0))
                                surface.blit(text_surface, (1000, 0))
                                my_font = pygame.font.SysFont('Comic Sans MS', 30)
                                text_surface = my_font.render("HI " + str(high), False, (0, 0, 0))
                                surface.blit(text_surface, (830, 0))
                            music = mixer.Sound("dino_death.wav")
                            music.play()
                            draw_spike()
                            time.sleep(3)
                            spike_x = 1300
                            score = 0
                            speed = 17
                        time.sleep(0.03)

                    for x in range(1, 10):
                        block_y += 12
                        spike_x -= speed
                        cloud_x -= speed/4
                        draw_spike()
                        draw_block()
                        draw_cloud()
                        score += 0.5
                        surface.blit(floor, (-40, -270))
                        text_surface = my_font.render(str(round(score)), False, (0, 0, 0))
                        surface.blit(text_surface, (1000, 0))
                        my_font = pygame.font.SysFont('Comic Sans MS', 30)
                        text_surface = my_font.render("HI " + str(high), False, (0, 0, 0))
                        surface.blit(text_surface, (830, 0))
                        if (score / 100).is_integer():
                            music = mixer.Sound("dino_score.wav")
                            music.play()
                            speed = speed * 1.1
                        if (block_x + int("30")) >= spike_x >= (block_x - int("30")) and block_y >= int("200"):
                            if score >= high:
                                high = round(score)
                                surface.blit(floor, (-40, -270))
                                text_surface = my_font.render(str(round(score)), False, (0, 0, 0))
                                surface.blit(text_surface, (1000, 0))
                                my_font = pygame.font.SysFont('Comic Sans MS', 30)
                                text_surface = my_font.render("HI " + str(high), False, (0, 0, 0))
                                surface.blit(text_surface, (830, 0))
                            music = mixer.Sound("dino_death.wav")
                            music.play()
                            draw_spike()
                            time.sleep(3)
                            spike_x = 1300
                            score = 0
                            speed = 17
                        time.sleep(0.03)

            elif event.type == QUIT:
                running = False
            else:
                while not keyboard.is_pressed("space"):
                    spike_x -= speed
                    cloud_x -= speed / 4
                    if (score / 2).is_integer():
                        block = pygame.image.load("dino_walk1.png").convert()
                    else:
                        block = pygame.image.load("dino_walk2.png").convert()
                    draw_spike()
                    draw_block()
                    draw_cloud()
                    score += 0.5
                    surface.blit(floor, (-40, -270))
                    text_surface = my_font.render(str(round(score)), False, (0, 0, 0))
                    surface.blit(text_surface, (1000, 0))
                    my_font = pygame.font.SysFont('Comic Sans MS', 30)
                    text_surface = my_font.render("HI " + str(high), False, (0, 0, 0))
                    surface.blit(text_surface, (830, 0))
                    if (score/100).is_integer():
                        music = mixer.Sound("dino_score.wav")
                        music.play()
                        speed = speed*1.1
                    if (block_x + int("30")) >= spike_x >= (block_x - int("30")) and block_y >= int("200"):
                        if score >= high:
                            high = round(score)
                            surface.blit(floor, (-40, -270))
                            text_surface = my_font.render(str(round(score)), False, (0, 0, 0))
                            surface.blit(text_surface, (1000, 0))
                            my_font = pygame.font.SysFont('Comic Sans MS', 30)
                            text_surface = my_font.render("HI " + str(high), False, (0, 0, 0))
                            surface.blit(text_surface, (830, 0))
                        music = mixer.Sound("dino_death.wav")
                        music.play()
                        draw_spike()
                        time.sleep(3)
                        spike_x = 1300
                        score = 0
                        speed = 17
                    time.sleep(0.03)
                    if spike_x <= int("-200"):
                        spike_x = 1300
                    if cloud_x <= int("-200"):
                        cloud_x = 1300
                        if random.random() >= 0.5:
                            cloud_y = 100
                        else:
                            cloud_y = 150
    else:
        while not keyboard.is_pressed("space"):
            if keyboard.is_pressed("1"):
                level = 1
            if keyboard.is_pressed("2"):
                level = 2
        menu = False
