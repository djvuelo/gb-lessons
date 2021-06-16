class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    """Pen"""

    def __init__(self):
        super().__init__('Ручка')

    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    """Pencil"""

    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        print('Запуск отрисовки каранашом')


class Handle(Stationery):
    """Handle"""

    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        print('Запуск отрисовки маркером')


new_pen = Pen()
new_pencil = Pencil()
new_handle = Handle()

new_pen.draw()
new_pencil.draw()
new_handle.draw()
