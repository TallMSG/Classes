from abc import ABC, abstractmethod

class Animal(ABC):
    name = 'unknown'
    need_for_food = 'голодный'
    need_for_collect = 'не обслужен'
    weight = 0

    def __init__(self, name='unknown'):
        self.name = name

    def feed(self):
        self.need_for_food = 'накормлен'

    def weigh(self, value):
        self.weight += value

    @abstractmethod
    def collect(self):
        pass

class Bird(Animal):
    eggs = 0

    def collect(self):
        self.need_for_collect = 'яйца собраны'

    def lay_eggs(self, value):
        self.eggs += value

class Cattle(Animal):

    def collect(self):
        self.need_for_collect = 'подоена'

class Sheep(Animal):

    def collect(self):
        self.need_for_collect = 'подстрижен'


goose1 = Bird('Гусь Серый')
goose2 = Bird('Гусь Белый')
duck1 = Bird('Утка Кря-кря')
hen1 = Bird('Курица Ко-ко')
hen2 = Bird('Курица Кукареку')
goat1 = Cattle('Коза Рога')
goat2 = Cattle('Коза Копыта')
cow1 = Cattle('Корова Манька')
sheep1 = Sheep('Баран Барашек')
sheep2 = Sheep('Баран Кудрявый')


animal_list = [goose1, goose2, duck1, hen1, hen2, goat1, goat2, cow1, sheep1, sheep2]



def weigh_all(an_list):
    goose1.weigh(11)
    goose2.weigh(10)
    duck1.weigh(9)
    hen1.weigh(5)
    hen2.weigh(7)
    goat1.weigh(35)
    goat2.weigh(37)
    cow1.weigh(305)
    sheep1.weigh(54)
    sheep2.weigh(65)

    total_name = [item.name for item in an_list]
    total_weight = [item.weight for item in an_list]
    print('Общий вес всех животных', sum(total_weight), 'кг')

    weight_animal_list = list(zip(total_name, total_weight))
    max_weight = max(item.weight for item in an_list)
    most_heavy_animal = max(weight_animal_list, key=lambda x: x[1])
    print('Самое тяжёлое животное - ', most_heavy_animal[0], ', ' 'вес составляет', max_weight, 'кг', )



def serve_all(an_list):
    for item in an_list:
        item.feed()
        item.collect()
        print(f'Животное: {item.name}')
        print('Необходимость кормления:', item.need_for_food)
        print('Необходимость обслуживания:', item.need_for_collect)
        print()


def main():
    weigh_all(animal_list)
    print()
    serve_all(animal_list)
    print('Все животные накормлены и обслужены')


main()



