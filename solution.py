def matrix_print(matrix):
    for line in matrix:
        print(line)


def refactor(field):
    matrix = [[] for i in range(len(field))]
    for i in range(len(field)):
        for j in range(len(field[i])):
            matrix[i].append(field[i][j].char())
    return matrix


class Field:
    def __init__(self, x, y):
        self.field = [[Cell() for i in range(x)] for i in range(y)]

    def get_field(self):
        return self.field

    def create_cell(self, x, y):
        self.field[y][x].revive()

    @staticmethod
    def near(field, x, y):
        counter = 0
        for ypos in range(y - 1, y + 2):
            for xpos in range(x - 1, x + 2):
                try:
                    if field[ypos][xpos] == 1:
                        counter += 1
                except:
                    continue

        if field[y][x] == 1:
            return counter - 1
        return counter

    def logic(self):
        f = list(refactor(self.get_field()))

        for y in range(len(self.get_field())):
            for x in range(len(self.get_field()[y])):

                if f[y][x] == 0 and self.near(f, x, y) == 3:
                    self.get_field()[y][x].revive()

                if f[y][x] == 1 and self.near(f, x, y) <= 1:
                    self.get_field()[y][x].kill()

                if f[y][x] == 1 and self.near(f, x, y) >= 4:
                    self.get_field()[y][x].kill()
        return


class Cell:
    def __init__(self):
        self.alive = False

    def is_alive(self):
        return self.alive

    def char(self):
        if self.is_alive():
            return 1
        return 0

    def kill(self):
        self.alive = False

    def revive(self):
        self.alive = True