class Movie:
    def __init__(self, title, duration, rating):
    
        self.title = title
        self.duration = duration
        self.rating = rating

    def increase_duration(self, minutes):
        
        self.duration += minutes
    
        if self.duration > 150:
            self.decrease_rating(0.5)

    def decrease_rating(self, amount):
        
        self.rating = max(self.rating - amount, 0)

    def display_info(self):
        
        return f"Nom: {self.title}, Davomiylik: {self.duration} minut, Reyting: {self.rating}"

movie1 = Movie("Oltin Yulduz", 120, 8.5)

movie1.increase_duration(40)  
print(movie1.display_info()) 