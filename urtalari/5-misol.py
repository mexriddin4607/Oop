class ShoppingCart:
    def __init__(self):
        self.cart = {} 

    def add_item(self, name, price):
    
        self.cart[name] = price

    def remove_item(self, name):
        
        if name in self.cart:
            del self.cart[name]
        else:
            print(f"{name} savatda topilmadi.")

    def get_total(self):
    
        return sum(self.cart.values())

cart = ShoppingCart()

while True:
    print("\n1. Mahsulot qo'shish")
    print("2. Mahsulot o'chirish")
    print("3. Savatdagi jami narxni ko'rsatish")
    print("4. Chiqish")
    
    choice = input("Tanlovni kiriting (1/2/3/4): ")
    
    if choice == '1':
        name = input("Mahsulot nomini kiriting: ")
        price = float(input("Mahsulot narxini kiriting: "))
        cart.add_item(name, price)
        print(f"{name} mahsuloti savatga qo'shildi.")
        
    elif choice == '2':
        name = input("O'chiriladigan mahsulot nomini kiriting: ")
        cart.remove_item(name)
        
    elif choice == '3':
        total = cart.get_total()
        print(f"Savatdagi jami narx: {total} so'm.")
        
    elif choice == '4':
        print("Chiqish...")
        break
    
    else:
        print("Noto'g'ri tanlov, qaytadan urinib ko'ring.")


