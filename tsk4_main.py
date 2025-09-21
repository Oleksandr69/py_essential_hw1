class CarForSale:
    def __init__(self, color: str, year: int, engine_volume: float, whell_drive: str):
        self.color = color
        self.year = year
        self.engine_volume = engine_volume
        self.whell_drive = whell_drive

    def __str__(self):
        result = f" {self.color}, {self.year}, {self.engine_volume}, {self.whell_drive}"
        return result

class CarDealership:
    def __init__(self, car_list: list):
        self.car_list = car_list

    def add_car(self):
        while True:
            print("==Введіть характеристики авто==")
            color_car = input(" Введіть колір: ")
            year_car = int(input("  Введіть рік випуску: "))
            engine_volume_car = float(input("   Введіть об'єм двигуна: "))
            whell_drive_car = input("    Який привід: ")
            value = input("Для виходу введіть 'stop': ")
            self.car_list.append(CarForSale(color=color_car, year=year_car, engine_volume=engine_volume_car, whell_drive=whell_drive_car))
            if value == "stop":
                break

    def __str__(self):
        result = ""
        for i, item in enumerate(self.car_list):
            result += (f"\n{i+1}. {item.__str__()}")
        return result

    def sell_a_car(self):
        print("Виберіть авто зі списку: ")
        self.__str__()
        number = int(input("Ваш вибір: ")) - 1
        if 0 <= number < len(self.car_list):
            sold_car = self.car_list.pop(number)
            print("Ви купили авто:")
            print(sold_car)
        else:
            print("Не вірний вибір..")

first_dealer_ship = CarDealership([])
first_dealer_ship.add_car()
print(first_dealer_ship)
print(repr(first_dealer_ship))
first_dealer_ship.sell_a_car()
print(first_dealer_ship)

# ================================================================
