from lesson_15.player import player_rect
from settings import *
import pytmx  # для работы с картой

# Загрузка карты TMX
map = pytmx.load_pygame("maps/карта.tmx")


def render_map():
    # ---------- Отрисовка карты TMX--------------#
    # Для каждого слоя карты
    for layer in map.visible_layers:
        # Для координат и id тайла в слое
        for x, y, gid in layer:
            # получаем изображения тайла
            tile = map.get_tile_image_by_gid(gid)
            # Если тайл определился (т.е. существует)
            if tile:
                # отрисовываем тайл в окне
                window.blit(tile, (x * map.tilewidth, y * map.tileheight))


# Функция для проверки столкновения коллизии игрока и тайла
def check_water_collision(tile_rect):
    if player_rect.colliderect(tile_rect):
        # Если правая сторона игрока пересекает левую сторону тайла
        if player_rect.right > tile_rect.left and player_rect.left < tile_rect.left:
            player_rect.right = tile_rect.left  # "выталкиваем" влево (заменяем правую границу игрока)

        # Если верхняя сторона игрока пересекает нижнюю сторону тайла
        elif player_rect.top < tile_rect.bottom and player_rect.bottom > tile_rect.bottom:
            player_rect.top = tile_rect.bottom  # Установка верхней стороны игрока на нижнюю сторону тайла


def render_map(camera_x, camera_y):
    #---------- Отрисовка карты TMX --------------#
    # Перебор видимых слоев карты
    for layer in map.visible_layers:
        # Перебор координат и идентификаторов тайлов в слое
        for x, y, gid in layer:
            # Получение изображения тайла по его глобальному идентификатору (GID)
            tile = map.get_tile_image_by_gid(gid)
            # Создание прямоугольника для позиционирования тайла на экране
            tile_rect = pygame.Rect(x * map.tilewidth + camera_x, y * map.tileheight + camera_y, map.tilewidth, map.tileheight)

            # Проверка столкновений с водой, если текущий слой - вода и тайл существует (gid != 0)
            if layer.name == 'вода' and gid != 0:
                check_water_collision(tile_rect)

            # Проверка на существование тайла перед отрисовкой
            if tile:
                # Отрисовка тайла на экране в окне приложения
                window.blit(tile, tile_rect)