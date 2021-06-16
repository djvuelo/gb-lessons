class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculate_tonna(self):
        return (self._length * self._width * 25 * 5) / 1000

    def __str__(self):
        return f'{self.mass_calculate_tonna()} т'


new_road_1 = Road(450, 5000)
print(new_road_1)
