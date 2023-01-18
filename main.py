import solution
import pygame as p
from pygame.locals import *

refactor = solution.refactor

SIZE = (500,500)
# Константы цветов RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Создаем окно
root = p.display.set_mode(SIZE)
field = solution.Field(root.get_width() // 20, root.get_height() // 20)



# Основной цикл


started = False
while True:

    root.fill(WHITE)


    for i in range(0 , root.get_height() // 20):
        p.draw.line(root , BLACK , (0 , i * 20) , (root.get_width() , i * 20))
    for j in range(0 , root.get_width() // 20):
        p.draw.line(root , BLACK, (j * 20 , 0) , (j * 20 , root.get_height()))

    # Проходимся по всем клеткам

    for i in range(0, len(refactor(field.get_field()))):
        for j in range(0, len(refactor(field.get_field())[i])):
            if refactor(field.get_field())[i][j] == 1:
                p.draw.rect(root, (255, 0, 0), [i * 20, j * 20, 20, 20])
    if not started:
        for i in p.event.get():
            if i.type == p.KEYDOWN:
                if i.key == p.K_s:
                    started = True
            pressed = p.mouse.get_pressed()
            pos = p.mouse.get_pos()
            if pressed[0]:
                field.create_cell(pos[1] // (SIZE[1] // len(field.get_field()[0])),
                                  pos[0] // (SIZE[0] // len(field.get_field())))

    p.display.update()
    if started:
        field.logic()
    for i in p.event.get():
        if i.type == QUIT:
            quit()
