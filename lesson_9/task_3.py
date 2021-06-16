class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": income, "bonus": 0}


class Position(Worker):

    def __init__(self, name, surname, position, income, bonus):
        super().__init__(name, surname, position, income)
        self.income["bonus"] = bonus

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return f'{self.income["wage"] + self.income["bonus"]} рублей оклад'


pos_1 = Position('Антуан', 'Лувуазье', 'главный химик', 50000, 10000)
pos_2 = Position('Песков', 'Петя', 'инженер', 20000, 5000)

print(pos_1.get_full_name())
print(pos_1.get_total_income())
print()
print(pos_2.get_full_name())
print(pos_2.get_total_income())
