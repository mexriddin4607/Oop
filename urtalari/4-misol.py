class Student:
    def __init__(self, ism, kurs, baho, stipendiya):
        self.ism = ism
        self.kurs = kurs
        self.baho = baho
        self.stipendiya = stipendiya

    def malumot_chiqarish(self):
        """Talaba haqida ma'lumot chiqarish."""
        return f"Ism: {self.ism}, Kurs: {self.kurs}, O'rtacha Baho: {self.baho}, Stipendiya: {self.stipendiya} so'm"

talabalar = []

for i in range(5):
    print(f"{i+1}-talaba:")
    ism = input("Ismi: ")
    kurs = input("O'qish kursi: ")
    baho = float(input("O'rtacha bahosi: "))
    stipendiya = float(input("Stipendiya miqdori (so'm): "))
    talaba = Student(ism, kurs, baho, stipendiya)
    talabalar.append(talaba)

print("\nO'rtacha bahosi 80 dan yuqori va stipendiyasi 1 million so'mdan katta bo'lgan talabalar:")
for talaba in talabalar:
    if talaba.baho > 80 and talaba.stipendiya > 1000000:
        print(talaba.malumot_chiqarish())
