class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def Display(self):
        print(f"name:{self.name}salary:{self.salary}")
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def Display(self):
        print(f"name:{self.name}salary:{self.salary}\n dept{self.department}")
e=Employee("tabbu",1000000)
m=Manager("lekh",23000,"cse")
e.Display()
m.Display()