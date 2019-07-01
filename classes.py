class Animal:
    name = 'unknown'
    voice = 'unknown'
    need_for_food = 'голодный'
    weight = 0

    def __init__(self, name='unknown'):
        self.name = name

    def feed(self):
        self.need_for_food = 'накормлен'

    def weigh(self, value):
        self.weight += value



class Bird(Animal):
    eggs = 0
    need_for_eggs = 'яйца не собраны'

    def gather_eggs(self):
        self.need_for_eggs = 'яйца собраны'

    def lay_eggs(self, value):
        self.eggs += value


class Goose(Bird):
    pass

goose1 = Goose('Серый')
goose2 = Goose('Белый')
goose1.weigh(11)
goose2.weigh(10)

class Duck(Bird):
    pass

duck1 = Duck('Кря-кря')
duck1.weigh(9)

class Hen(Bird):
    pass

hen1 = Hen('Ко-ко')
hen2 = Hen('Кукареку')
hen1.weigh(5)
hen2.weigh(7)

class Cattle(Animal):
    need_for_milk = 'недояна'

    def milk(self):
        self.need_for_milk = 'подоена'


class Goat(Cattle):
    pass

goat1 = Goat('Рога')
goat2 = Goat('Копыта')
goat1.weigh(35)
goat2.weigh(37)

class Cow(Cattle):
    pass

cow1 = Cow('Манька')
cow1.weigh(305)

class Sheep(Animal):
    need_for_shear = 'не подстрижен'

    def shear(self):
        self.need_for_shear = 'подстрижен'

sheep1 = Sheep('Барашек')
sheep2 = Sheep('Кудрявый')
sheep1.weigh(54)
sheep2.weigh(65)

animal_list = [goose1, goose2, duck1, hen1, hen2, goat1, goat2, cow1, sheep1, sheep2]
cattle_list = [goat1, goat2, cow1]
sheeps_list = [sheep1, sheep2]
birds_list = [goose1, goose2, duck1, hen1, hen2]

total_weight = [item.weight for item in animal_list]
total_name = [item.name for item in animal_list]
print('Общий вес всех животных', sum(total_weight), 'кг')

weight_animal_list = list(zip(total_name, total_weight))


max_weight = max(item.weight for item in animal_list)
most_heavy_animal = max(weight_animal_list, key=lambda x: x[1])
print('Самое тяжёлое животное - ', most_heavy_animal[0],', ' 'вес составляет', max_weight, 'кг', )




def feed_all(an_list):
    for item in an_list:
        item.feed()
        print(item.name, item.need_for_food)

def milk_all(an_list):
    for item in an_list:
        item.milk()
        print(item.name, item.need_for_milk)

def shear_all(an_list):
    for item in an_list:
        item.shear()
        print(item.name, item.need_for_shear)

def gather_eggs_all(an_list):
    for item in an_list:
        item.gather_eggs()
        print(item.name, item.need_for_eggs)


def main():
    feed_all(animal_list)
    milk_all(cattle_list)
    shear_all(sheeps_list)
    gather_eggs_all(birds_list)
    print('Все животные обслужены')


main()



