class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property: {self.address}, {self.area} sq. meters, {self.rooms} rooms, ${self.price}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House: {self.address}, {self.area} sq. meters, {self.rooms} rooms, ${self.price}, Plot size: {self.plot} sq. meters"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat: {self.address}, {self.area} sq. meters, {self.rooms} rooms, ${self.price}, Floor: {self.floor}"


house1 = House(area=150, rooms=4, price=250000, address="ul. Kwiatowa 5", plot=500)
flat1 = Flat(area=80, rooms=3, price=150000, address="ul. Nowa 10", floor=2)

print(house1)
print(flat1)

