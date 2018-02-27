class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.

    def add_item(self, name, price):
        self.items.append({"name":name, "price":price})
        # Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        total = 0
        for item in self.items:
            totClasses and objectsal += sum(item["price"])
        return total
        # Add together all item prices in self.items and return the total.

#--------------------------
class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5,9,12,3,1,21)
    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer("Rolf")
player_one.numbers = (1,2,3,4,5,6)
player_two = LotteryPlayer("John")


#--------------------------

class Student:
    def __init__(self, name, school, marks):
        self.name = "John"
        self.school = "Harvard"
        self.marks = marks
    def average(self):
        return sum(self.marks)/len(self.marks)

anna = Student ("Anna", "MiT", [1,2,3])
anna
anna.marks
anna.marks.append(123)
anna.marks

#--------------------------
class Student:
    def __init__(self, name, school, marks):
        self.name = "John"
        self.school = "Harvard"
        self.marks = marks
    def average(self):
        return sum(self.marks)/len(self.marks)
    @classmethod
    def go_to_school(cls):
        return "I'm going to school"
        return "I'm a {}".format(cls)
    @staticmethod
    def go_to_school_stat():
        return "static:I'm going to school"


anna = Student ("Anna", "MiT", [1,2,3])
anna
anna.marks
anna.marks.append(123)
anna.marks

anna = Student("Anna", "Oxford", [1,2,3])
rolf = Student("Rolf", "Harvard", [4,5,6])

print(anna.go_to_school())
print(rolf.go_to_school())
