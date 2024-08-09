class House:
    def __init__(self, name, numb):
        self.name = name
        self.numbers_of_floors = numb


    def go_to(self, new_floor):
        if new_floor > self.numbers_of_floors or new_floor < 1:
            print('Такого этажа не существует')
            return
        for i in range(1, new_floor + 1):
            print(i)


    def __len__(self):
        return self.numbers_of_floors


    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.numbers_of_floors}"


    def __eq__(self, other):
        if isinstance(other, int):
            return self.numbers_of_floors == other
        return self.numbers_of_floors == other.numbers_of_floors


    def __lt__(self, other):
        if isinstance(other, int):
            return self.numbers_of_floors < other
        return self.numbers_of_floors < other.numbers_of_floors


    def __le__(self, other):
        if isinstance(other, int):
            return self.numbers_of_floors <= other
        return self.numbers_of_floors <= other.numbers_of_floors


    def __gt__(self, other):
        if isinstance(other, int):
            return self.numbers_of_floors > other
        return self.numbers_of_floors > other.numbers_of_floors


    def __ge__(self, other):
        if isinstance(other, int):
            return self.numbers_of_floors >= other
        return self.numbers_of_floors >= other.numbers_of_floors


    def __ne__(self, other):
        if isinstance(other, int):
            return self.numbers_of_floors != other
        return self.numbers_of_floors != other.numbers_of_floors


    def __add__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors += value
        return self


    def __radd__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors += value
        return self


    def __iadd__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors += value
        return self


house1 = House("ЖК Эльбрус", 10)
house2 = House("ЖК Воробьёвы горы", 20)
print(house1)
print(house2)

print(house1 == house2) # __eq__

house1 = house1 + 10 # __add__
print(house1)
print(house1 == house2)

house1 += 10 # __iadd__
print(house1)

house2 = 10 + house2 # __radd__
print(house2)

print(house1 > house2) # __gt__
print(house1 >= house2) # __ge__
print(house1 < house2) # __lt__
print(house1 <= house2) # __le__
print(house1 != house2) # __ne__
