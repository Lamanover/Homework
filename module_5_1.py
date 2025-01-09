class house:
    def __init__(self, name, number_of_flors):
        self.name = name
        self.number_of_flors = number_of_flors

    def go_to(self, new_floor):
        if self.number_of_flors >= new_floor:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')



h1 = house('ЖК Горский', 18)
h2 = house('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)