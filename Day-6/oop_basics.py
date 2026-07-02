class student:
    def __init__(self,name, grade):
        self.name = name
        self.grade = grade
    def study(self):
        print(f"{self.name} is studying in grade {self.grade}")
student1= student("Bhuvana", "A+")
student2= student("Harsh", "A+")
student1.study()
student2.study()
