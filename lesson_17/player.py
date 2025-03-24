from settings import * # подключаем настройки

# Загрузка изображений для анимации  спрайта по умолчанию
player_anim_stop = []

for frame in range(0, 6):
  image = pygame.image.load(f'images/player/стоит/{frame}.png').convert_alpha()
  player_anim_stop.append(image)

player_anim_up = pygame.image.load(f'images/player/вверх/0.png')
player_anim_down = pygame.image.load(f'images/player/вниз/0.png')
player_anim_left = pygame.image.load(f'images/player/влево/0.png')
player_anim_right = pygame.image.load(f'images/player/вправо/0.png')
player_anim_attack = pygame.image.load(f'images/player/атака/0.png')


current_frame = 0 # устанавливаем текущий кадр анимации

# Загрузка и изменение размеров изображения игрока
player_image = player_anim_stop[0]
# Уменьшаем размеры изображения
player_image = pygame.transform.scale(player_image, (32, 32))



# Создание прямоугольника коллизий для игрока
player_rect = player_image.get_rect()

# Начальная позиция игрока
player_rect.centerx = WINDOW_WIDTH // 2
player_rect.centery = WINDOW_HEIGHT // 2

# Скорость перемещения игрока (дробное значение)
player_speed = 0.6
player_speed_x = 0
player_speed_y = 0

# функция отрисовки игрока и его анимации
def render_player(player_rect, animation: list = player_anim_stop):
  global current_frame # объявляем глобальную переменную current_frame
  
  # Обновление кадра анимации
  current_frame = current_frame + 1

  if current_frame == len(animation):
    current_frame = 0

  # Отображение текущего кадра анимации спрайта
  window.blit(animation[current_frame], player_rect)


# функция перемещение персонажа игрока 
def movement_player( player_speed_x,  player_speed_y):
  global player_rect

  #перемещаем спрайт 
  player_rect.centerx += player_speed_x
  player_rect.centery += player_speed_y
