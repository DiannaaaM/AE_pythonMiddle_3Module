import pygame
import pytmx
from player import player_rect
from settings import *

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
