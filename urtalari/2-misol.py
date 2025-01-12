class Restaurant:
    def __init__(self, nomi):
        self.nomi = nomi

    def menyu(self):

        pass

    def narxlar(self):
        
        pass

class FastFood(Restaurant):
    def __init__(self, nomi):
        super().__init__(nomi)

    def menyu(self):
        return ["Burger", "Fries", "Soda"]

    def narxlar(self):
        return {"Burger": 5000, "Fries": 3000, "Soda": 2000}

class FineDining(Restaurant):
    def __init__(self, nomi):
        super().__init__(nomi)

    def menyu(self):
        return ["Steak", "Lobster", "Truffle Pasta"]

    def narxlar(self):
        return {"Steak": 3000, "Lobster": 5000, "Truffle Pasta": 4000}

fast_food_restaurant = FastFood("QuickBite")
print(f"{fast_food_restaurant.nomi} Menyusi: {fast_food_restaurant.menyu()}")
print(f"{fast_food_restaurant.nomi} Narxlari: {fast_food_restaurant.narxlar()}")

fine_dining_restaurant = FineDining("The Gourmet Spot")
print(f"{fine_dining_restaurant.nomi} Menyusi: {fine_dining_restaurant.menyu()}")
print(f"{fine_dining_restaurant.nomi} Narxlari: {fine_dining_restaurant.narxlar()}")
