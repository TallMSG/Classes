class Animals:
    name = 'unknown'  # Animal name
    voice = 'unknown'  # Animal's voice
    need_for_food = 'голодный'  # Need for food
    weight = 0  # Animal's weight, kg

    def __init__(self, name='unknown'):
        self.name = name

    # def givname(self):
    #     self.name = input('Enter mame: ')

    def feed(self):
        self.need_for_food = 'накормлен'

    def weigh(self, value):
        self.weight += value



class Birds(Animals):
    eggs = 0  # Count of eggs
    need_for_eggs = 'яйца не собраны'  # Eggs gathered or not

    def gather_eggs(self):
        self.need_for_eggs = 'яйца собраны'

    def lay_eggs(self, value):
        self.eggs += value


class Geese(Birds):
    pass

goose1 = Geese('Серый')
goose2 = Geese('Белый')
goose1.weigh(11)
goose2.weigh(10)

class Ducks(Birds):
    pass

duck1 = Ducks('Кря-кря')
duck1.weigh(9)

class Hens(Birds):
    pass

hen1 = Hens('Ко-ко')
hen2 = Hens('Кукареку')
hen1.weigh(5)
hen2.weigh(7)

class Cattle(Animals):
    need_for_milk = 'недояна'  # Cattle milked or not

    def milk(self):
        self.need_for_milk = 'подоена'


class Goats(Cattle):
    pass

goat1 = Goats('Рога')
goat2 = Goats('Копыта')
goat1.weigh(35)
goat2.weigh(37)

class Cows(Cattle):
    pass

cow1 = Cows('Манька')
cow1.weigh(305)

class Sheeps(Animals):
    need_for_shear = 'не пострижен'  # Sheeps sheared or not

    def shear(self):
        self.need_for_shear = 'пострижен'

sheep1 = Sheeps('Барашек')
sheep2 = Sheeps('Кудрявый')
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



# for item in animal_list:
#     w = item.weight
#     print(item.name, w, 'кг')



# animal_dict = {'animals': animal_list, 'cattle': cattle_list, 'sheeps': sheeps_list, 'birds': birds_list}
# print(animal_dict)


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



