import pygame
# Загрузка спрайт-листа
sprite_sheet = pygame.image.load("sprite/Arcade - The Simpsons - Bart Devil-Photoroom0.png")
# Отзеркаливание спрайта
flipped_sprite = pygame.transform.flip(sprite_sheet, True, False)


