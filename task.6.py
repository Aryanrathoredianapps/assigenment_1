class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("the name is",self.name)
        print("the age is",self.age)

class Student(Person):
    def __init__(self, name, age, section):
        Person.__init__(self,name,age)
        self.section=section

    def display_student(self):
        print("the name is",self.name)
        print("the age is",self.age)
        print("the section is",self.section)
# o=Person("aryan" , "22")
# o.display()
obj=Student("aryan",'22','A')
obj.display_student()