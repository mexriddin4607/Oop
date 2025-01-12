class School:
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar = []  

    def talabani_qoshish(self, talaba):
    
        self.talabalar.append(talaba)

    def talabani_ochirish(self, talaba):
    
        if talaba in self.talabalar:
            self.talabalar.remove(talaba)
            print(f"{talaba} ro'yxatdan o'chirildi.")
        else:
            print(f"{talaba} ro'yxatda topilmadi.")

    def talabalar_ro_yxati(self):
        
        return ', '.join(self.talabalar)


maktab = School("Najot talim maktabi")


maktab.talabani_qoshish("Mexriddin")
maktab.talabani_qoshish("Abdurasul")
maktab.talabani_qoshish("Suxrob")
maktab.talabani_qoshish("Asror")
maktab.talabani_qoshish("Olim")

print("Talabalar ro'yxati:", maktab.talabalar_ro_yxati())

talaba_ochirish = input("Ro'yxatdan o'chiriladigan talabani kiriting: ")

maktab.talabani_ochirish(talaba_ochirish)

print("Yangilangan talabalar ro'yxati:", maktab.talabalar_ro_yxati())
