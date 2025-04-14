from  settings import *
import pytmx # для работы с картой


# Загрузка карты TMX
map = pytmx.load_pygame("Tiled/tilemap-example-a.tmx")



def render_map():
   #---------- Отрисовка карты TMX--------------#
   # Для каждого слоя карты
    for layer in map.visible_layers:

        # Для координат и id тайла в слое
        for x, y, gid in layer:

            #получаем изображения тайла
            tile = map.get_tile_image_by_gid(gid)

            #Если тайл определился (т.е. существует)
            if tile:
                #отрисовываем тайл в окне
                window.blit(tile, (x * map.tilewidth, y * map.tileheight))