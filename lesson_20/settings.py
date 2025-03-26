#-----------------------------настройки игры----------------------------------#
import json
import os

import pygame, sys  # Импорт библиотек pygame и sys для работы с графикой и системными функциями соответственно
from pygame.locals import QUIT  # Импорт константы QUIT из pygame.locals для обработки событий выхода из программы

pygame.init()  # Инициализация pygame

# Установка размера окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Установка заголовка окна
pygame.display.set_caption('Это шаблон')

# Определение нежно синего цвета в формате RGB
NEON_BLUE = (173, 216, 230)

# Создание объекта Clock для управления FPS
clock = pygame.time.Clock()
FPS = 30  # Устанавливаем желаемое количество кадров в секунду
#-----------------------------настройки игры----------------------------------#

# Допустим, у нас есть словарь с данными игры
game_data = {

}

# Функция для сохранения данных игры
def save_game(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_game(filename, player_rect):
    global camera_x, camera_y

    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        player_rect.x, player_rect.y = data['player_pos']
        camera_x, camera_y = data['camera_pos']
