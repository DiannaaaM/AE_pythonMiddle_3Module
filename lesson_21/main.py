# -----------------------------настройки игры----------------------------------#
from sys import platform

import pygame, sys  # Импорт библиотек pygame и sys для работы с графикой и системными функциями соответственно
from pygame.locals import QUIT  # Импорт константы QUIT из pygame.locals для обработки событий выхода из программы

from lesson_21.map import render_map

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


# -------------------------------Игровой цикл-------------------------------------#
# Бесконечный цикл для отображения окна и обработки событий
while True:
    # Заполнение окна нежно синим цветом
    window.fill(NEON_BLUE)
    render_map()
    # Обработка событий pygame
    for event in pygame.event.get():
        # Если событие - выход из программы
        if event.type == QUIT:
            pygame.quit()  # Завершение работы pygame
            sys.exit()  # Завершение программы

    # Ограничение FPS
    clock.tick(FPS)

    pygame.display.update()  # Обновление содержимого окна
# -------------------------------Игровой цикл-------------------------------------#
