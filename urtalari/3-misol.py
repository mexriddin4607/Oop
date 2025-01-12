class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def get_average(self):

        return sum(self.grades) / len(self.grades)

    def is_passing(self):
        
        return self.get_average() > 60

students = []

num_students = int(input("Qancha talaba kiritmoqchisiz? "))

for i in range(num_students):
    print(f"\n{i+1}-talaba:")
    name = input("Ismi: ")
    age = int(input("Yoshi: "))
    
    grades_input = input("Baholarni kiriting (vergul bilan ajratilgan): ")
    grades = list(map(int, grades_input.split(',')))
    
    student = Student(name, age, grades)
    students.append(student)

for student in students:
    print(f"\n{student.name} o'rtacha bahosi: {student.get_average()} - Is Passing: {student.is_passing()}")
