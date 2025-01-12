class Avtomobil:
    def __init__(self, marka, model, yil, narx):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.narx = narx

    def chiqarish(self):
        return f"Marka: {self.marka}, Model: {self.model}, Yil: {self.yil}, Narx: ${self.narx}"

avtomobillar = []
for i in range(5):
    print(f"{i + 1}-avtomobil uchun ma'lumot kiriting:")
    marka = input("Markasi: ")
    model = input("Modeli: ")
    yil = int(input("Ishlab chiqarilgan yili: "))
    narx = float(input("Narxi ($): "))
    avtomobillar.append(Avtomobil(marka, model, yil, narx))
    print()

print("2010-yildan katta bo'lgan avtomobillar:")
for avtomobil in avtomobillar:
    if avtomobil.yil > 2010:
        print(avtomobil.chiqarish())