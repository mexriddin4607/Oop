
class Employee:
    def __init__(self, ism, oylik_maosh):
        
        self.ism = ism
        self.oylik_maosh = oylik_maosh

    def yillik_maosh(self):
    
        return self.oylik_maosh * 12


xodim1 = Employee("Mexriddin Axmedov", 2000)

print(f"{xodim1.ism}ning yillik maoshi: ${xodim1.yillik_maosh()}")

print('Ooo zurku maniyam shogirtlikka oling 😂')
