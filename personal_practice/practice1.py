class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class Employee(Person):
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
    def getId(self):
        return self.id


a = Employee("IoT", 65, 2018)
print(a.getName(), a.getAge(), a.getId())