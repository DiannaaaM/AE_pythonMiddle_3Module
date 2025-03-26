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


def render_text(surface, text):
    # Рендер текста в поверхность
    text_surface = font.render(text, True, (255, 255, 255))  # Создаем объект Surface для текста
    surface.blit(text_surface, (0, 0))


# Определение размера и шрифта текста
font = pygame.font.SysFont(name='Arial', size=48)

# Создание текстового объекта
text = font.render("", True, (255, 255, 255))

# Определение коллизии текста
text_stage_rect = text.get_rect()
text_stage_rect.center = (WINDOW_WIDTH // 2, 50)
