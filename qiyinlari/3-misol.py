class Manager:
    def __init__(self, name, position, work_hours, salary):
        self.name = name
        self.position = position
        self.work_hours = work_hours
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Work Hours: {self.work_hours}, Salary: {self.salary}"

employees = [
    Manager("Ali", "Rahbar", 45, 5000000),
    Manager("Vali", "Xodim", 38, 3000000),
    Manager("Mexriddin", "Rahbar", 50, 5500000),
    Manager("Aziz", "Mutaxassis", 42, 4000000),
    Manager("Asror", "Rahbar", 39, 4800000),
    Manager("Olim", "Texnik", 41, 3500000),
    Manager("Abdurasul", "Rahbar", 44, 5200000),
]

filtered_employees = [emp for emp in employees if emp.work_hours > 40 and emp.position == "Rahbar"]

for emp in filtered_employees:
    print(emp)
