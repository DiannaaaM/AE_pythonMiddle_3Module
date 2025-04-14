from settings import *

import pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
# Загрузка спрайт-листа
sprite_sheet = pygame.image.load("sprite/Arcade - The Simpsons - Bart Devil-Photoroom0.png")
# Отзеркаливание спрайта
flipped_sprite = pygame.transform.flip(sprite_sheet, True, False)
sprite_sheet = pygame.transform.scale(sprite_sheet, (32, 32))
flipped_sprite = pygame.transform.scale(flipped_sprite, (32, 32))
player_rect = sprite_sheet.get_rect()


def render_player(player_rect):
    window.blit(sprite_sheet, player_rect)

# Функция перемещения персонажа игрока
def movement_player(player_speed_x, player_speed_y):
    global player_rect

    # Перемещаем спрайт
    player_rect.centerx += player_speed_x
    player_rect.centery += player_speed_y

    # Ограничение движения персонажа в границах окна
    if player_rect.left < 0:
        player_rect.left = 0
    elif player_rect.right > WINDOW_WIDTH:
        player_rect.right = WINDOW_WIDTH
    if player_rect.top < 0:
        player_rect.top = 0
    elif player_rect.bottom > WINDOW_HEIGHT:
        player_rect.bottom = WINDOW_HEIGHT


def movement_camera(player_rect, map_width, map_height):
    camera_x = -player_rect.x + WINDOW_WIDTH // 2
    camera_y = -player_rect.y + WINDOW_HEIGHT // 2

    camera_x = min(0, camera_x)  # left
    camera_y = min(0, camera_y)  # top
    camera_x = max(-(map_width - WINDOW_WIDTH), camera_x)  # right
    camera_y = max(-(map_height - WINDOW_HEIGHT), camera_y)  # bottom

    return camera_x, camera_y


