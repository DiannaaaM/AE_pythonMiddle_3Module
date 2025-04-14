from settings import *  # подключаем настройки
import math

enemy_speed_y = 0.6
enemy_speed_x = 0.5

# -------------------------Добавьте код самостоятельно--------------#
# Загрузка изображений для анимации  спрайта по умолчанию
enemy_anim_stop = []

for frame in range(1, 4):
    image = pygame.image.load(
        f'enemy/Custom Edited - Mario Customs - Pokey Sunshine Design SMW-Style-Photoroom{frame}.png').convert_alpha()
    enemy_anim_stop.append(image)

# Устанавливаем текущий кадр анимации
current_frame_enemy = 0

# Загрузка и изменение размеров изображения противника
enemy_image = enemy_anim_stop[0]
enemy_image = pygame.transform.scale(enemy_image, (32, 32))

# Создание прямоугольника коллизий для противника
enemy_rect = enemy_image.get_rect()

# Начальная позиция противника
enemy_rect.centerx = 200
enemy_rect.centery = 200


# Функция отрисовки противника и его анимации
def render_enemy(enemy_rect, animation: list = enemy_anim_stop):
    global current_frame_enemy  # объявляем глобальную переменную

    # Обновление кадра анимации
    current_frame_enemy += 1
    if current_frame_enemy == len(animation):
        current_frame_enemy = 0

    # Отображение текущего кадра анимации спрайта
    window.blit(animation[current_frame_enemy], enemy_rect)


def movement_enemy(player_rect, enemy_rect):
    # Определяем разницу по осям между игроком и противником
    delta_x = player_rect.centerx - enemy_rect.centerx
    delta_y = player_rect.centery - enemy_rect.centery

    # Движение врага в сторону игрока
    if abs(delta_x) > abs(delta_y):
        if delta_x > 0:
            enemy_rect.x += enemy_speed_x  # Движение вправо
        else:
            enemy_rect.x -= enemy_speed_x  # Движение влево
    else:
        if delta_y > 0:
            enemy_rect.y += enemy_speed_y  # Движение вниз
        else:
            enemy_rect.y -= enemy_speed_y  # Движение вверх

    # Проверка границ экрана
    if enemy_rect.left < 0:
        enemy_rect.left = 0
    if enemy_rect.right > window.get_width():
        enemy_rect.right = window.get_width()
    if enemy_rect.top < 0:
        enemy_rect.top = 0
    if enemy_rect.bottom > window.get_height():
        enemy_rect.bottom = window.get_height()