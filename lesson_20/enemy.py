from settings import *  # подключаем настройки

# -------------------------Добавьте код самостоятельно--------------#
# Загрузка изображений для анимации  спрайта по умолчанию
enemy_anim_stop = []

is_alive_enemy = True

enemy_speed_x = 0.5
enemy_speed_y = 0.6

# Загрузка изображений для анимации бега спрайта по умолчанию
for frame in range(1, 16):
    image = pygame.image.load(f'противник/{frame}.png').convert_alpha()
    enemy_anim_stop.append(image)
# устанавливаем текущий кадр анимации
current_frame_enemy = 0
# Загрузка и изменение размеров изображения противника
enemy_image = enemy_anim_stop[0]
# Уменьшаем размеры изображения
enemy_image = pygame.transform.scale(enemy_image, (32, 32))

# Создание прямоугольника коллизий для противника
enemy_rect = enemy_image.get_rect()

# Начальная позиция противника
enemy_rect.centerx = 200
enemy_rect.centery = 200


# Скорость перемещения противника (дробное значение)
# ------------------------Добавьте код самостоятельно------------------


# функция отрисовки противника и его анимации
def render_enemy(enemy_rect, animation: list = enemy_anim_stop):
    global current_frame_enemy  # объявляем глобальную переменную

    # Обновление кадра анимации
    current_frame_enemy += 1
    if current_frame_enemy == len(animation):
        current_frame_enemy = 0

    # Отображение текущего кадра анимации спрайта
    window.blit(animation[current_frame_enemy], enemy_rect)


def movement_enemy(player_rect, enemy_rect):
    # Игрок справа от противника?
    if player_rect.centerx >= enemy_rect.centerx:
        enemy_rect.x += enemy_speed_x

    # Игрок справа от противника?
    elif player_rect.centerx <= enemy_rect.centerx:
        enemy_rect.x -= enemy_speed_x

    elif player_rect.centery >= enemy_rect.centery:
        enemy_rect.y += enemy_speed_y

    elif player_rect.centery <= enemy_rect.centery:
        enemy_rect.y -= enemy_speed_y
