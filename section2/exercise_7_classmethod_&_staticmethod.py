class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return "{}, total stock price: {}".format(store.name, int(store.stock_price()))


store = Store("Test")
print ("store.name:", store.name)
store2 = Store("Amazon")
print ("store2.name:", store2.name)
store2.add_item("Keyboard", 160)

Store.franchise(store)  # returns a Store with name "Test - franchise"
print ("store.name:", store.name)
Store.franchise(store2)  # returns a Store with name "Amazon - franchise"
print ("store2.name:", store2.name)

print (Store.store_details(store))  # returns "Test, total stock price: 0"
print (Store.store_details(store2) ) # returns "Amazon, total stock price: 160"