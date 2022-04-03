class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(2, 8)
print(p.x)  ## 2
print(p.y)  ## 8

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Goku", "Saitama", "Seiya", "Gojo", "Naruto"]
for person in people:
    sucess = flight.add_passenger(person)
    if sucess:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")

