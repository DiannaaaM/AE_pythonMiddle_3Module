import pygame
import sys
import pytmx

from lesson_17.npc import render_npc, render_text
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

# Set up the display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Загадочный остров')

# Define colors
NEON_BLUE = (173, 216, 230)

# Set up the clock
clock = pygame.time.Clock()
FPS = 30

# Load the TMX map
map = pytmx.load_pygame("maps/карта.tmx")

# Get map dimensions
map_width = map.width * map.tilewidth
map_height = map.height * map.tileheight

# Initialize camera
camera_x = 0
camera_y = 0

# Initialize player
player_rect = pygame.Rect(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 32, 32)
playerx_speed = 0
playery_speed = 0

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

# Начальные координаты NPC
npc_x = 100  # Фиксированная позиция по оси X
npc_y = 150  # Фиксированная позиция по оси Y
npc_image = pygame.image.load(f'images/player/стоит/1.png').convert_alpha()  # Загрузка изображения NPC

# Функция для отрисовки NPC
def render_npc(surface):
    surface.blit(npc_image, (npc_x + camera_x, npc_y + camera_y))  # Рендерим NPC на фиксированной позиции

# Функция для отрисовки текста
def render_text(surface, text):
    font = pygame.font.SysFont('Arial', 48)
    text_surface = font.render(text, True, (255, 255, 255))
    surface.blit(text_surface, (0, 0))

# Main game loop
while True:
    window.fill(NEON_BLUE)  # Заливаем окно цветом NEON_BLUE

    # Отрисовка карты
    for layer in map.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                if gid:
                    tile = map.get_tile_image_by_gid(gid)
                    if tile:
                        window.blit(tile, ((x * map.tilewidth) + camera_x, (y * map.tileheight) + camera_y))

    # Draw player using the render_player function
    render_player(pygame.Rect(player_rect.x + camera_x, player_rect.y + camera_y, player_rect.width, player_rect.height))

    for event in pygame.event.get():
        # Проверка на закрытие окна
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

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
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                playerx_speed = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                playery_speed = 0

    # Вызов функции для перемещения игрока
    movement_player(playerx_speed, playery_speed)

    # Обновление позиции камеры
    camera_x, camera_y = movement_camera(player_rect, map_width, map_height)

    # Рендер текста
    render_text(window, "эээээЭЭЭ")  # Рендерим строку на экране
    render_npc(window)  # Рендерим NPC

    pygame.display.update()  # Обновляем экран
    clock.tick(FPS)  # Ограничиваем FPS
