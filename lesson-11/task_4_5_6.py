from abc import ABC
from exeptions import OfficeEquipmentModelError, OfficeEquipmentColorError, DepartamentNameError, \
    AppendEquipmentTypeError, WarehouseCompanyNameError, AppendDepartamentTypeError


class Departament:
    def __init__(self, name):
        self.__name = name
        self.office_equipments = []

    @classmethod
    def name(cls, name):
        if not isinstance(name, str):
            raise DepartamentNameError(name)
        return cls(name)

    def equipment(self, *off_eqs):
        for off_eq in off_eqs:
            if not type(off_eq) in OfficeEquipment.__subclasses__():
                raise AppendEquipmentTypeError(off_eq,
                                               [str(classname.__name__) for classname in
                                                OfficeEquipment.__subclasses__()])
        self.office_equipments += list(off_eqs)
        return self

    def __str__(self):
        output = ' ' * 3 + f'- Подразделение: "{self.__name}" -> (Доступная оргтехника):\n'
        if not self.office_equipments:
            output += ' ' * 8 + '- Нет оргтехники'
        else:
            for oeq in self.office_equipments:
                output += ' ' * 8 + str(oeq)
        return output + '\n'


class Warehouse:
    """Склад оргтехники"""

    def __init__(self, name):
        self.__departaments = []
        self.__name = name

    @classmethod
    def company(cls, name):
        if not isinstance(name, str):
            raise WarehouseCompanyNameError(name)
        return cls(name)

    def departaments(self, *departaments):
        for departament in departaments:
            if not type(departament) == Departament:
                raise AppendDepartamentTypeError(departament, Departament.__name__)
        self.__departaments += list(departaments)
        return self

    def move_equipment(self, from_departament, to_departament, equipment):
        from_departament.office_equipments.remove(equipment)
        to_departament.office_equipments.append(equipment)
        return self

    def __str__(self):
        output = f'Склад компании "{self.__name}" -> (Подразделения):\n'
        if not self.__departaments:
            output += ' ' * 3 + '- Нет подразделений'
        else:
            for depo in self.__departaments:
                output += str(depo)
        return output


class OfficeEquipment(ABC):
    """Оргтехника"""

    def __init__(self, model, name=None, color=None):
        self.__properties = {'name': name, 'model': model, 'color': color}

    @classmethod
    def model(cls, model):
        if not isinstance(model, str):
            raise OfficeEquipmentModelError(model)
        return cls(model)

    def color(self, color):
        if not isinstance(color, str):
            raise OfficeEquipmentColorError(color)
        self.__properties['color'] = color
        return self

    def __str__(self):
        return f'{self.__properties["name"]}({self.__properties["model"]}), цвет: {self.__properties["color"]}\n'


class Printer(OfficeEquipment):
    """Принтер"""

    def __init__(self, model):
        super().__init__('Принтер', model)


class Scanner(OfficeEquipment):
    """Сканер"""

    def __init__(self, model):
        super().__init__('Сканер', model)


class Xerox(OfficeEquipment):
    """Ксерокс"""

    def __init__(self, model):
        super().__init__('Ксерокс', model)


'''
Обзор структуры
'''
try:
    '''
    Оргтехника
    '''
    printer_lenovo = Printer.model('Lenovo RX3').color('белый')
    scanner_asus = Scanner.model('ASUS VKD8').color('синий')
    xerox_dns = Xerox.model('DNS ERT8').color('красный')

    '''
    Департаменты
    '''
    tech = Departament.name("Технический отдел").equipment(printer_lenovo, scanner_asus)
    adv = Departament.name("Отдел рекламы").equipment(xerox_dns)

    '''
    Структура склада
    '''
    ware = Warehouse.company('GeekBrains').departaments(tech, adv)
    print(ware)
    '''
    Перемещение оборудования из одного депртамента в другой
    '''
    print(f'Перемещение ({str(printer_lenovo)[:-1]}) из одного департамента в другой:\n\n')
    print(ware.move_equipment(tech, adv, printer_lenovo))
except (
        OfficeEquipmentModelError, OfficeEquipmentColorError, DepartamentNameError,
        AppendEquipmentTypeError, AppendDepartamentTypeError) as error:
    print(error)
