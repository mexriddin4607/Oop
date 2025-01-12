class Telefon:
    def __init__(self, nomi, ram, narx, kompaniya):
        self.nomi = nomi
        self.ram = ram
        self.narx = narx
        self.kompaniya = kompaniya

    def chiqarish(self):
        return f"Nomi: {self.nomi}, RAM: {self.ram} GB, Narxi: ${self.narx}, Kompaniya: {self.kompaniya}"

telefonlar = [
    Telefon("Samsung Galaxy S21", 8, 999, "Samsung"),
    Telefon("iPhone 13", 4, 1099, "Apple"),
    Telefon("Redmi Note 11", 6, 299, "Xiaomi"),
    Telefon("Realme C11", 2, 149, "Realme"),
]

print("RAM hajmi 2 GB dan ko'p va 8 GB dan kichik telefonlar:")
for telefon in telefonlar:
    if 2 < telefon.ram < 8:
        print(telefon.chiqarish())