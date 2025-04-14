import pygame
import pytmx

# Загрузка карты TMX
map = pytmx.load_pygame("Tiled/tilemap-example-a.tmx")

def check_collision(player_rect, tile_rect):
    if player_rect.colliderect(tile_rect):
        # Если правая сторона игрока пересекает левую сторону тайла
        if player_rect.right > tile_rect.left and player_rect.left < tile_rect.left:
            player_rect.right = tile_rect.left  # "выталкиваем" влево
        # Если левая сторона игрока пересекает правую сторону тайла
        elif player_rect.left < tile_rect.right and player_rect.right > tile_rect.right:
            player_rect.left = tile_rect.right  # "выталкиваем" вправо
        # Если верхняя сторона игрока пересекает нижнюю сторону тайла
        elif player_rect.top < tile_rect.bottom and player_rect.bottom > tile_rect.bottom:
            player_rect.top = tile_rect.bottom  # Установка верхней стороны игрока на нижнюю сторону тайла
        # Если нижняя сторона игрока пересекает верхнюю сторону тайла
        elif player_rect.bottom > tile_rect.top and player_rect.top < tile_rect.top:
            player_rect.bottom = tile_rect.top  # Установка нижней стороны игрока на верхнюю сторону тайла

def render_map(camera_x, camera_y, window, player_rect):
    #---------- Отрисовка карты TMX --------------#
    for layer in map.visible_layers:
        for x, y, gid in layer:
            tile = map.get_tile_image_by_gid(gid)
            tile_rect = pygame.Rect(x * map.tilewidth + camera_x, y * map.tileheight + camera_y, map.tilewidth, map.tileheight)
            # Проверка и отображение коллизий
            if gid != 0 and layer.name == 'Tiles':  # Проверяем только тайлы, у которых есть изображение
                check_collision(player_rect, tile_rect)
            if tile:
                window.blit(tile, (x * map.tilewidth + camera_x, y * map.tileheight + camera_y))
