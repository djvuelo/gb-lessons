class Cell:
    def __init__(self, count):
        self.count = count

    def make_order(self, cell_on_line):
        cell_output = ''
        count_lines = int(self.count / cell_on_line)
        trash = self.count - count_lines * cell_on_line
        for cell in range(0, count_lines):
            cell_output += '*' * cell_on_line + '\n'
        cell_output += '*' * trash + '\n'
        return cell_output

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(int(self.count / other.count))


cell1 = Cell(20)
cell2 = Cell(3)

print('cell1 + cell2: \n' + (cell1 + cell2).make_order(5))
print('cell1 - cell2: \n' + (cell1 - cell2).make_order(5))
print('cell1 * cell2: \n' + (cell1 * cell2).make_order(5))
print('cell1 / cell2: \n' + (cell1 / cell2).make_order(5))
