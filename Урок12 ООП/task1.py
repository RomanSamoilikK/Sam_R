# Class-далее название клааса
# тело класса.
class Car:
    color= "Grey" # свойства
    # Статические поля(переменные класса)
    default_color = "Grey"
    default_weight = 5000

    def __init__(self, color, model):
        # Динамические поля(переменные объекта)
        self.color = color
        self.model = model

    def turn_on(self):
        pass
    def ride(self):
        pass
car_object = "Car"
print(dir(Car))

def turn_on(self):
    pass

