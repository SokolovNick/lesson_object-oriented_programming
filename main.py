class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def __str__(self):
        return f"Store: {self.name}, Address: {self.address}, Items: {self.items}"

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def get_price(self, name):
        return self.items.get(name)

    def update_price(self, name, new_price):
        if name in self.items:
            self.items[name] = new_price


store1 = Store("Pobeda", "Omsk, st. Lenina 1")
store2 = Store("Magnit", "Omsk, st. Frunze 14")
store3 = Store("Pyatyorochka", "Omsk, st. Zhukova 6")

store1.add_item("apple", 20)
store1.add_item("banana", 30)
store1.add_item("orange", 40)

store2.add_item("sugar", 50)
store2.add_item("salt", 45)
store2.add_item("cookies", 60)

store3.add_item("burger", 80)
store3.add_item("coffee", 100)
store3.add_item("tea", 75)

print(store1)
print(store2)
print(store3)

print(store1.get_price("apple"))
store1.update_price("apple", 25)
print(store1.get_price("apple"))

store1.remove_item("banana")
print(store1)
