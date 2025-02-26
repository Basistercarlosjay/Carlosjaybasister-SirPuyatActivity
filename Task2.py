class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, I'm {self.name}. an {self.age} year-old {self.course} student.")

student1 = Student("Carlos Jay Basister",21, "Information Technology")
student2 = Student("Cjay Basister", 21, "Culinary")
student3 = Student("CJ Basister", 21, "Education")

print("Student 1:")
student1.introduce()
print("\nStudent 2:")
student2.introduce()
print("\nStudent 3:")
student3.introduce()
