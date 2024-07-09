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


my_house = House('Brusnika', 17)
brosers_house = House('Seasons', 9)
mothers_house = House('Krulov', 5)

my_house.go_to(7)
brosers_house.go_to(5)
mothers_house.go_to(9)