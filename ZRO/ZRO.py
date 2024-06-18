import pygame
import sys
import math

# Инициализация Pygame
pygame.init()

# Настройки окна
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Интерактивный текст ZRO с анимацией волны')

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Координаты точек для каждой буквы (сдвиг на 60 шагов вправо)
letters = {
    'Z': [(160, 200), (180, 200), (200, 200), (220, 200), (240, 200),
          (240, 220), (220, 240), (200, 260), (180, 280), (160, 300),
          (160, 320), (180, 320), (200, 320), (220, 320), (240, 320)],
    'R': [(360, 200), (360, 220), (360, 240), (360, 260), (360, 280),
          (360, 300), (380, 200), (400, 200), (420, 200), (440, 220),
          (440, 240), (420, 260), (400, 260), (380, 260), (400, 280),
          (420, 300), (440, 320), (360, 320)],
    'O': [(560, 200), (580, 200), (600, 200), (620, 200), (640, 220),
          (640, 240), (640, 260), (640, 280), (640, 300), (620, 320),
          (600, 320), (580, 320), (560, 320), (540, 300), (540, 280),
          (540, 260), (540, 240), (540, 220)],
}

# Размер точки
point_radius = 10

# Основной игровой цикл
running = True
start_time = pygame.time.get_ticks()
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение фона черным цветом
    window.fill(black)

    # Получение позиции курсора
    mouse_pos = pygame.mouse.get_pos()

    # Текущее время в миллисекундах
    current_time = pygame.time.get_ticks() - start_time

    # Рисование точек для каждой буквы с проверкой наведения курсора
    for letter, points in letters.items():
        for i, point in enumerate(points):
            # Вычисление расстояния от курсора до точки
            distance = math.sqrt((point[0] - mouse_pos[0]) ** 2 + (point[1] - mouse_pos[1]) ** 2)
            if distance < 100:  # Если курсор находится в пределах 100 пикселей от точки
                wave_offset = math.sin(current_time * 0.005 + distance / 10) * 2.5  # Уменьшенная амплитуда колебаний волны в 2.5 раза
                animated_point = (point[0], point[1] + wave_offset)
            else:
                animated_point = point

            # Изменение цвета точки при наведении
            if (animated_point[0] - point_radius <= mouse_pos[0] <= animated_point[0] + point_radius) and (animated_point[1] - point_radius <= mouse_pos[1] <= animated_point[1] + point_radius):
                color = red
            else:
                color = white
            pygame.draw.circle(window, color, animated_point, point_radius)

    # Обновление дисплея
    pygame.display.flip()

    # Ограничение FPS
    pygame.time.Clock().tick(60)

# Завершение работы Pygame
pygame.quit()
sys.exit()
