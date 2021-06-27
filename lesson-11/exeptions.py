class DayError(Exception):
    """Exeption for Date class"""

    def __init__(self, message):
        self.message = message


class MonthError(Exception):
    """Exeption for Date class"""

    def __init__(self, message):
        self.message = message


class YearError(Exception):
    """Exeption for Date class"""

    def __init__(self, message):
        self.message = message


class DateError(Exception):
    """Exeption for Date class"""

    def __init__(self, message):
        self.message = message


class DivError(ZeroDivisionError):
    """Error division by zero"""

    def __init__(self, denominator):
        super().__init__(f"Division {denominator} error: don't do this bullshit")


class OfficeEquipmentModelError(Exception):
    """Error Equipment model name"""

    def __init__(self, value):
        super().__init__(f"OfficeEquipmentModelError ({value}): must be str")


class OfficeEquipmentColorError(Exception):
    """Error Equipment name"""

    def __init__(self, value):
        super().__init__(f"OfficeEquipmentColorError ({value}): must be str")


class DepartamentNameError(Exception):
    """Error Departament name"""

    def __init__(self, value):
        super().__init__(f"DepartamentNameError ({value}): must be str")


class AppendEquipmentTypeError(Exception):
    """Error type adding Equipment in Departanment"""

    def __init__(self, value, classes):
        super().__init__(f"AppendEquipmentTypeError ({value}): must be some object from classes ({classes})")


class WarehouseCompanyNameError(Exception):
    """Error company name of warehouse"""

    def __init__(self, value):
        super().__init__(f"WarehouseCompanyNameError ({value}): must be str")


class AppendDepartamentTypeError(Exception):
    """Error type adding Departament in Warehouse"""

    def __init__(self, value, classes):
        super().__init__(f"AppendDepartamentTypeError ({value}): must be some object from classes ({classes})")
