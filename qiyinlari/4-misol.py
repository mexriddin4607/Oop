class Student:
    def __init__(self, name, average_grade, is_grant, stipend):
        self.name = name
        self.average_grade = average_grade
        self.is_grant = is_grant
        self.stipend = stipend

    def input_student(self, name, average_grade, is_grant, stipend):
        self.name = name
        self.average_grade = average_grade
        self.is_grant = is_grant
        self.stipend = stipend

    def __str__(self):
        return f"Name: {self.name}, Average Grade: {self.average_grade}, Grant: {self.is_grant}, Stipend: {self.stipend}"

students = [
    Student("Ali", 90, True, 1000000),
    Student("Vali", 80, False, 0),
    Student("Mexriddin", 88, True, 1200000),
    Student("Aziz", 75, True, 900000),
    Student("Asror", 92, True, 1300000),
]

filtered_students = [student for student in students if student.is_grant and student.average_grade > 85]

for student in filtered_students:
    print(student)
