import pygame
import pytmx
import sys
from pygame.locals import QUIT
from player import sprite_sheet, flipped_sprite, render_player
from lesson_23.player import movement_player, movement_camera
from enemy import render_enemy, enemy_rect, movement_enemy

# Инициализация pygame
pygame.init()

# Создаем окно для отображения
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Загрузка карты TMX
map = pytmx.load_pygame("Tiled/tilemap-example-a.tmx")


# Функция для проверки столкновения игрока и тайла
def check_collision(player_rect, tile_rect):
    if player_rect.colliderect(tile_rect):
        if player_rect.right > tile_rect.left and player_rect.left < tile_rect.left:
            player_rect.right = tile_rect.left
        elif player_rect.left < tile_rect.right and player_rect.right > tile_rect.right:
            player_rect.left = tile_rect.right
        elif player_rect.top < tile_rect.bottom and player_rect.bottom > tile_rect.bottom:
            player_rect.top = tile_rect.bottom
        elif player_rect.bottom > tile_rect.top and player_rect.top < tile_rect.top:
            player_rect.bottom = tile_rect.top


def render_map(camera_x, camera_y):
    for layer in map.visible_layers:
        for x, y, gid in layer:
            tile = map.get_tile_image_by_gid(gid)
            tile_rect = pygame.Rect(x * map.tilewidth + camera_x, y * map.tileheight + camera_y, map.tilewidth,
                                    map.tileheight)
            if gid != 0 and layer.name == 'Tiles':
                check_collision(player_rect, tile_rect)
            if tile:
                window.blit(tile, (x * map.tilewidth + camera_x, y * map.tileheight + camera_y))


# Теперь продолжаем основной код для игры
# Инициализация микшера
pygame.mixer.init()
pygame.mixer.music.load("../lesson_23/little-dreamers.mp3")
pygame.mixer.music.play(-1)

# Установка заголовка окна
pygame.display.set_caption('Индивидуальный проект')
NEON_BLUE = (173, 216, 230)

# Создание объекта Clock для управления FPS
clock = pygame.time.Clock()
FPS = 30
player_rect = sprite_sheet.get_rect()
player_rect.topleft = (100, 100)
player_speed = 5
current_sprite = sprite_sheet
is_alive_player = True
is_alive_enemy = True
while True:

    window.fill(NEON_BLUE)

    camera_x, camera_y = movement_camera(player_rect, map.width * map.tilewidth, map.height * map.tileheight)

    render_map(camera_x, camera_y)

    window.blit(current_sprite, player_rect.topleft)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_rect.x -= player_speed
                current_sprite = flipped_sprite
            elif event.key == pygame.K_RIGHT:
                player_rect.x += player_speed
                current_sprite = sprite_sheet
            elif event.key == pygame.K_UP:
                player_rect.y -= player_speed
            elif event.key == pygame.K_DOWN:
                player_rect.y += player_speed

    if is_alive_player:
        render_player(player_rect)
    else:
        break

    if is_alive_enemy:
        render_enemy(enemy_rect)
        movement_enemy(player_rect, enemy_rect, 0.5, 0.5)

        if enemy_rect.colliderect(player_rect):
            is_alive_player = False  # Игрок проигрывает, когда враг его догоняет

    clock.tick(FPS)
    pygame.display.update()
