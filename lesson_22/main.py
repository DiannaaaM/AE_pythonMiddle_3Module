# -----------------------------настройки игры----------------------------------#
from sys import platform

import pygame, sys  # Импорт библиотек pygame и sys для работы с графикой и системными функциями соответственно
from pygame.locals import QUIT  # Импорт константы QUIT из pygame.locals для обработки событий выхода из программы

from lesson_21.map import render_map, map
from player import sprite_sheet, flipped_sprite

pygame.init()  # Инициализация pygame

# Установка размера окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Установка заголовка окна
pygame.display.set_caption('Индивидуальный проект')

# Определение нежно синего цвета в формате RGB
NEON_BLUE = (173, 216, 230)

# Создание объекта Clock для управления FPS
clock = pygame.time.Clock()
FPS = 30  # Устанавливаем желаемое количество кадров в секунду

# -----------------------------настройки игры----------------------------------#
playerx = -3
playery = 115
current_sprite = sprite_sheet  # Текущий спрайт по умолчанию
# -------------------------------Игровой цикл-------------------------------------#
# Бесконечный цикл для отображения окна и обработки событий
while True:
    # Заполнение окна нежно синим цветом
    window.fill(NEON_BLUE)

    # Отрисовка карты и спрайта
    render_map()
    window.blit(current_sprite, (playerx, playery))

    # Обработка событий pygame
    for event in pygame.event.get():
        # Если событие - выход из программы
        if event.type == QUIT:
            pygame.quit()  # Завершение работы pygame
            sys.exit()  # Завершение программы
        # Обработка нажатий клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_speed = -5  # Установка скорость перемещения влево
                current_sprite = flipped_sprite
            elif event.key == pygame.K_RIGHT:
                playerx_speed = 5  # Установка скорость перемещения вправо
                current_sprite = sprite_sheet
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                playerx_speed = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                playery_speed = 0

    # Ограничение FPS
    clock.tick(FPS)

    pygame.display.update()  # Обновление содержимого
# -------------------------------Игровой цикл-------------------------------------#
