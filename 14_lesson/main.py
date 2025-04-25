from map import * # подключаем наш модуль 

# Основной цикл программы
while True:

    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отрисовка карты TMX
    render_map()

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(FPS)

# Завершение работы Pygame
pygame.quit()