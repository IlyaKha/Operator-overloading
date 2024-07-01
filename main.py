class House:
    def __init__(self, name, numberOfFloors):

         self.name = name
         self.numberOfFloors = numberOfFloors

    def __eq__(self, other):
        #Сравниваем количество этажей
        if isinstance(other, House):
            return self.numberOfFloors == other.numberOfFloors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.numberOfFloors < other.numberOfFloors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.numberOfFloors <= other.numberOfFloors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.numberOfFloors > other.numberOfFloors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.numberOfFloors >= other.numberOfFloors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.numberOfFloors != other.numberOfFloors
        return False

    def __add__(self, value):
        if isinstance(value, int):
            self.numberOfFloors += value
            return self
        return False

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __str__(self):
     #Преобразование в строку для вывода.
        return f"Название: {self.name}, кол-во этажей: {self.numberOfFloors}"

# Пример выполняемого кода:
h1 = House('ЖК Каспий', 10)
h2 = House('ЖК Гранатовый', 20)

print(h1)
print(h2)
print(h1 == h2)
h1 = h1 + 10
print(h1)
print(h1 == h2)
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
