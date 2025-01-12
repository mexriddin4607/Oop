
class Student:
    def __init__(self, first_name, last_name, course, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.average_grade = average_grade

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


student1 = Student("Mexriddin", "Axmedov","1","90")

print(student1.get_full_name())  
