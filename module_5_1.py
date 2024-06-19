class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1:
            print('Такого этажа не существует')
        for i in range(1, new_floor + 1):
            if new_floor <= self.number_of_floors:
                print(i)
                continue
            else:
                print('Такого этажа не существует')
            break


point_of_route1 = House('ЖК "Летний сад"', 10)
point_of_route2 = House('ЖК "Дом у озера"', 5)


point_of_route1.go_to(5)
point_of_route2.go_to(0)
