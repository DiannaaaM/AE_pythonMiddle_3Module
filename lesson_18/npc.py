import pygame

from settings import *  # Убедитесь, что настройки правильные

# Initialize Pygame
pygame.init()

# Set up the display
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Загадочный остров')

# Загрузка изображений для NPC

npc_image = pygame.image.load(f'images/player/стоит/1.png').convert_alpha()

# Начальная позиция NPC
npc_x = 100  # Укажите стартовые координаты NPC
npc_y = 150
npc_rect = pygame.Rect(npc_x, npc_y, 32, 32)  # Создание прямоугольника коллизий для NPC

# Скорость движения NPC, если это необходимо
npc_speed = 1


# Функция для отрисовки NPC и его анимации
def render_npc(surface):
    global npc_image  # Объявляем глобальную переменную current_npc_frame

    # Отображение текущего кадра анимации NPC
    surface.blit(npc_image, (npc_rect.x, npc_rect.y))

# Инициализация переменных для квеста "Потерянный ключ"
talked_to_merchant = False  # Флаг, указывающий на то, что игрок поговорил с торговцем
found_key = False  # Флаг, указывающий на то, что игрок нашел ключ
opened_chest = False  # Флаг, указывающий на то, что игрок открыл сундук


# Функция для отображения текста
def render_text(surface, text, font):
    text_surface = font.render(text, True, (255, 255, 255))  # Создаем объект Surface для текста
    surface.blit(text_surface, (0, 0))


# Логика квеста find_the_key
def find_the_key(npc_rect, player_rect, key_rect, treasure_chest_rect, font, surface):
    global talked_to_merchant, found_key, opened_chest

    # Проверка взаимодействия с торговцем
    if player_rect.colliderect(npc_rect):
        talked_to_merchant = True

    # Проверка нахождения ключа игроком
    if talked_to_merchant and player_rect.colliderect(key_rect):
        found_key = True

    # Проверка открытия сундука с помощью ключа
    if talked_to_merchant and found_key and player_rect.colliderect(treasure_chest_rect):
        opened_chest = True

    # Отображение подсказок в зависимости от состояния квеста
    text = ""
    if not talked_to_merchant:
        text = "Поговорите с торговцем."
    elif talked_to_merchant and not found_key:
        text = "Торговец говорит: 'Ключ потерялся возле большого дерева в лесу.'"
    elif found_key and not opened_chest:
        text = "Найдите сундук и откройте его с помощью ключа."
    elif opened_chest:
        text = "Поздравляем! Вы нашли сокровища в сундуке!"

    # Отображение текста
    return render_text(surface, text, font)


# Определение размера и шрифта текста
font = pygame.font.SysFont(name='Arial', size=14)

# Создание текстового объекта
text = font.render("", True, (255, 255, 255))

# Определение коллизии текста
text_stage_rect = text.get_rect()
text_stage_rect.center = (WINDOW_WIDTH // 2, 50)
