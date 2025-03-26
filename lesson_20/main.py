import pygame
import sys
import pytmx

from lesson_19.npc import render_npc, render_text, npc_rect
from lesson_19.player import quests_visible, display_quests
from lesson_19.npc import find_the_key
from lesson_19.settings import save_game, load_game
from lesson_20.enemy import render_enemy, enemy_rect, is_alive_enemy, movement_enemy
from lesson_20.player import draw_hp_bar, player_anim_attack, is_alive_player, is_attack
from player import (
    player_anim_up,
    player_anim_down,
    player_anim_left,
    player_anim_right,
    player_rect,
    player_speed,
    render_player,
)

# Initialize Pygame
pygame.init()

# Инициализация микшера
pygame.mixer.init()

# Загрузка и воспроизведение фоновой музыки
pygame.mixer.music.load("C:/Users/M.CREATOR/PycharmProjects/AE_pythonMiddle_3Module/lesson_18/little-dreamers.mp3")
pygame.mixer.music.play(-1)

# Установки окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Загадочный остров')

# Инициализация цветов
NEON_BLUE = (173, 216, 230)

# Инициализация часов
clock = pygame.time.Clock()
FPS = 30

# Загрузка карты
map = pytmx.load_pygame("maps/карта.tmx")

# Получение размеров карты
map_width = map.width * map.tilewidth
map_height = map.height * map.tileheight

# Инициализация камеры
camera_x = 0
camera_y = 0

# # Инициализация игрока
player_rect = pygame.Rect(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 32, 32)
playerx_speed = 0
playery_speed = 0
player_hp = 50
# Инициализация шрифта
font = pygame.font.SysFont(name='Arial', size=48)


def movement_player(x_speed, y_speed):
    player_rect.x += x_speed
    player_rect.y += y_speed


def movement_camera(player_rect, map_width, map_height):
    camera_x = -player_rect.x + WINDOW_WIDTH // 2
    camera_y = -player_rect.y + WINDOW_HEIGHT // 2

    camera_x = min(0, camera_x)  # left
    camera_y = min(0, camera_y)  # top
    camera_x = max(-(map_width - WINDOW_WIDTH), camera_x)  # right
    camera_y = max(-(map_height - WINDOW_HEIGHT), camera_y)  # bottom

    return camera_x, camera_y


# Загружаем данные игры
load_game('savegame.json', player_rect)

# Главный игровой цикл
while True:
    game_data = {'player_pos': (player_rect.x, player_rect.y),
                 'camera_pos': (camera_x, camera_y),
                 }
    window.fill(NEON_BLUE)  # Заливаем окно цветом NEON_BLUE

    # Перебор видимых слоев карты
    for layer in map.visible_layers:
        # Перебор координат и идентификаторов тайлов в слое
        for x, y, gid in layer:
            # Получение изображения тайла по его глобальному идентификатору (GID)
            tile = map.get_tile_image_by_gid(gid)
            # Создание прямоугольника для позиционирования тайла на экране
            tile_rect = pygame.Rect(x * map.tilewidth + camera_x, y * map.tileheight + camera_y, map.tilewidth,
                                    map.tileheight)

            # Проверка на существование тайла перед отрисовкой
            if tile:
                # Отрисовка тайла на экране в окне приложения
                window.blit(tile, tile_rect)

    # Создание прямоугольников для ключа и сундука
    key_rect = pygame.Rect(200, 200, 32, 32)  # Пример прямоугольника для ключа
    treasure_chest_rect = pygame.Rect(300, 300, 32, 32)  # Пример прямоугольника для сундука

    # Вызов функции квеста
    quest_text = find_the_key(npc_rect, player_rect, key_rect, treasure_chest_rect, font,
                              window)  # Вызов функции квеста


    if is_alive_player:
        render_player(player_rect)

    if is_alive_enemy:
        render_enemy(enemy_rect)

    if player_rect.colliderect(enemy_rect):
        if is_attack:
        # Уничтожаем противника
            is_alive_enemy = False
        else:
            # Уменьшаем HP игрока
            if player_hp > 0:
                player_hp -= 1  # Пример уменьшения HP
            else:
                player_hp = 0  # Чтобы HP не становился отрицательным

    # Рисуем HP бар
    draw_hp_bar(player_hp)

    # Отображение текста квеста
    if quest_text:  # Проверяем, что текст не пуст
        render_text(window, quest_text, font)

    movement_enemy(player_rect, enemy_rect)

    for event in pygame.event.get():
        # Проверка на закрытие окна
        if event.type == pygame.QUIT:
            game_data = {'player_pos': (player_rect.x, player_rect.y),
                         'camera_pos': (camera_x, camera_y),
                         }
            save_game('savegame.json', game_data)
            running = False
            break

        # Обработка нажатий клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerx_speed = player_speed
            elif event.key == pygame.K_LEFT:
                playerx_speed = -player_speed
            elif event.key == pygame.K_UP:
                playery_speed = -player_speed
            elif event.key == pygame.K_DOWN:
                playery_speed = player_speed
            elif event.key == pygame.K_SPACE:
                animation = player_anim_attack
                is_attack = True
            elif event.key == pygame.K_o:  # Сохранение игры
                save_game('savegame.json', game_data)
            elif event.key == pygame.K_l:  # Загрузка игры
                load_game('savegame.json', player_rect)
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                playerx_speed = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                playery_speed = 0

    # Вызов функции для перемещения игрока
    movement_player(playerx_speed, playery_speed)

    # Обновление позиции камеры
    camera_x, camera_y = movement_camera(player_rect, map_width, map_height)

    render_npc(window)  # Рендерим NPC
    pygame.display.update()  # Обновляем экран
    clock.tick(FPS)  # Ограничиваем FPS
