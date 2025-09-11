class Student:
    def __init__(self,rollno,name,marks):
        self.rollno=rollno
        self.name=name
        self.marks=marks
    def Display(self):
        print(f"name:{self.name}\n rollno:{self.rollno}\nmarks{self.marks}\n")
s=Student(12,"sony",76)
s1=Student(9,"alice",89)
s. Display()
s1.Display()