class Dokon:
    def __init__(self, nomi, joylashuvi, mahsulot_turi, ish_vaqti):
        self.nomi = nomi
        self.joylashuvi = joylashuvi
        self.mahsulot_turi = mahsulot_turi
        self.ish_vaqti = ish_vaqti

    def chiqarish(self):
        return f"Nomi: {self.nomi}, Joylashuvi: {self.joylashuvi}, Mahsulot turi: {self.mahsulot_turi}, Ish vaqti: {self.ish_vaqti}"

dokolar = []
for i in range(5):
    print(f"{i + 1}-do'kon uchun ma'lumot kiriting:")
    nomi = input("Do'kon nomi: ")
    joylashuvi = input("Joylashuvi: ")
    mahsulot_turi = input("Mahsulot turi: ")
    ish_vaqti = input("Ish vaqti: ")
    dokolar.append(Dokon(nomi, joylashuvi, mahsulot_turi, ish_vaqti))
    print()

print("Mahsulot turi 'Elektronika' bo'lgan do'konlar:")
for dokon in dokolar:
    if dokon.mahsulot_turi.lower() == "elektronika":
        print(dokon.chiqarish())