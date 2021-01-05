def add(*args):
    print(sum(list(args)))


print(add(3, 5, 6))


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        # print(key)
        # print(value)
        n += kwargs["add"]
        n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Nissan", model="GT-R")
print(my_car)
print(my_car.make)
print(my_car.color) #will return None because of .get()

