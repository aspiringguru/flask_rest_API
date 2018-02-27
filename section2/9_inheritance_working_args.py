class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(marks) / len(marks)

    @classmethod
    def friend(cls, origin, friend_name, *args):
        #return another student in same school with different name
        return cls(friend_name, origin.school, salary)


"""
anna = Student("Anna", "Oxford")
print (anna)
print (anna.name, anna.school, anna.marks)

friend = anna.friend("Greg")
print(friend.name, friend.school, friend.marks)

print ("WorkingStudent_ below")
class WorkingStudent_(Student):
    pass

anna2 = WorkingStudent_("Anna", "Oxford")
print (anna2)
print (anna2.name, anna2.school, anna2.marks)

friend2 = anna2.friend("Greg")
print(friend2.name, friend2.school, friend2.marks)
"""


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


anna = WorkingStudent("Anna", "Harvard", 20.00)
print("anna.salary:", anna.salary)
print ("type(anna):", type(anna))

sue = WorkingStudent.friend(anna, "Sue", 17.50)
print ("type(sue):", type(sue))
print("sue.name:", sue.name)
print("sue.school:", sue.school)
print("sue.salary:", sue.salary)  # Error!

