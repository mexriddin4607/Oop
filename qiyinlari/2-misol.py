class Instrument:
    def __init__(self, name, price, manufacturer, type_):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.type_ = type_

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Manufacturer: {self.manufacturer}, Type: {self.type_}"


instruments = [
    Instrument("Piano", 3000000, "Yamaha", "klaviatura"),
    Instrument("Violin", 1500000, "Stradivarius", "struna"),
    Instrument("Guitar", 2500000, "Fender", "struna"),
    Instrument("Keyboard", 2200000, "Casio", "klaviatura"),
    Instrument("Flute", 800000, "Yamaha", "puflama"),
    Instrument("Drum", 1800000, "Pearl", "zarbli"),
    Instrument("Organ", 4000000, "Hammond", "klaviatura"),
]

# Narxi 2 mln somdan yuqori va turi klaviatura bo‘lganlarni chiqaramiz
filtered_instruments = [instr for instr in instruments if instr.price > 2000000 and instr.type_ == "klaviatura"]

for instr in filtered_instruments:
    print(instr)
