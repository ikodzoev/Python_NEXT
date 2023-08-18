"""Доработаем задания 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики."""


class Animal():
    def __init__(self, kind, name, age):
        self._kind = kind
        self._name = name
        self._age = age

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1


class Fishes(Animal):

    def __init__(self, kind, name, age, size):
        super().__init__(kind, name, age)
        self._size = size

    def get_specific(self):
        return self._size


class Birds(Animal):

    def __init__(self, kind, name, age, color):
        super().__init__(kind, name, age)
        self._color = color

    def get_specific(self):
        return self._color


class Mammals(Animal):

    def __init__(self, kind, name, age, spec):
        super().__init__(kind, name, age)
        self._spec = spec

    def get_specific(self):
        return self._spec


class AnimalFactory:
    def __init__(self, animal_type, **kwargs):
        self.animal_type = animal_type
        self.kwargs = kwargs

    def create_animal(self):
        return self.animal_type(**self.kwargs)


f1 = Fishes('Карась', 'Федя', 1, 15)
print(f'Вид: {f1.get_kind()}')
print(f'кличка: {f1.get_name()}')
print(f'возраст: {f1.get_age()} лет')
print(f'размер: {f1.get_specific()} см.')

fish_factory = AnimalFactory(Fishes, kind='Карась', name='Федя', age=1, size=15)
fish = fish_factory.create_animal()
print(f'Вид: {fish.get_kind()}')
print(f'кличка: {fish.get_name()}')
print(f'возраст: {fish.get_age()} лет')
print(f'размер: {fish.get_specific()} см.')
