class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        self.new_floor = 1
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            print(new_floor)

    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f'Название {self.name}, Количество {self.number_of_floors}'


my_house = House('Brusnika', 17)
brosers_house = House('Seasons', 9)
mothers_house = House('Krulov', 5)

my_house.go_to(7)
brosers_house.go_to(5)
mothers_house.go_to(9)

print(len(my_house))
print(len(brosers_house))
print(len(mothers_house))

print(my_house)
print(brosers_house)
print(mothers_house)
