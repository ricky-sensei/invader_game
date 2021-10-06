"""
9/25
後で変数名等リファクタリングが必要
9/29
１時間目：blitの説明まで→ifによる上下左右への動き
2時間目：上下左右の移動→押しっぱなし処理
コミットすることを教える
"""

import pygame
from pygame.locals import *

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("インベーダーゲーム")
screen.fill((0, 0, 0))

player = pygame.image.load("player.png")
playerX = 100
playerY = 200

running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(player, (playerX, playerY))

    # 押されたキーを調べる
    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_LEFT]:
        playerX -= 0.1
        print(key_pressed)
    if key_pressed[K_RIGHT]:
        playerX += 0.1



    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # if event.type == KEYDOWN:
        #     if event.key == K_LEFT:
        #         playerX -= 1
        #

    pygame.display.update()
