# Simple Inheritance

class city():
    def __init__(self, Cname):
        self.Cname = Cname 
    def city_name(self):
        print(self.Cname)

class street(city):
    def __init__(self, Cname, sName):
        super().__init__(Cname)
        self.sName = sName
    def street_name(self):
        print(self.sName)

address = street("Paris", "25th Street")
address.city_name()
address.street_name()

# Multilevel Inheritance

class Food:
    def __init__(self, Energy):
        self.Energy = Energy
    def energyPrint(self):
        print(self.Energy)

class Sweets(Food):
    def __init__(self, Energy):
        super().__init__(Energy)
        self.Taste = "Sweet"
    def taste(self):
        print(self.Taste)

class Chocolate(Sweets):
    def __init__(self, Energy):
        super().__init__(Energy)
        self.Texture = "Smooth"
    def texture(self):
        print(self.Texture)

chocolateBar = Chocolate("100 kCal")
chocolateBar.texture()
chocolateBar.taste()
chocolateBar.energyPrint()

# Multiple Inheritance

class Phone:
    def __init__(self, number):
        self.number = number
    def call(self):
        print("Calling: ", self.number)

class Laptop:
    def __init__(self, email):
        self.email = email
    def Email(self):
        print("Emailing: ", self.email)

class Tablet(Phone, Laptop):
    def __init__(self, drawing, email, number):
        Laptop.__init__(self, email)
        Phone.__init__(self, number)
        self.drawing = drawing
    def drawDisplay(self):
        print(self.drawing)

Tablet1 = Tablet("Art", "JohnDoe@gmail.com", "1231231234")
Tablet1.drawDisplay()
Tablet1.Email()
Tablet1.call()

# Hierarchical Inheritance

class Appliances:
    def __init__(self, Exists):
        self.Exists = Exists
    def PlugIn(self):
        print("Plugged In, ready to be operated.")

class Fridge(Appliances):
    def __init__(self, brand, model_year, cubic_area):
        self.brand = brand
        self.model_year = model_year
        self.cubic_area = cubic_area
    def cool(self):
        print("Fridge is cooling food.")

class TV(Appliances):
    def __init__(self, brand, quality, surface_area):
        self.brand = brand
        self.quality = quality
        self.surface_area = surface_area
    def Display(self):
        print("TV is displaying media.")

fridge1 = Fridge("LG", 2020, "25 ft^3")
print("Fridge brand: ", fridge1.brand)
print("Fridge model year: ", fridge1.model_year)
print("Fridge storage capacity: ", fridge1.cubic_area)
fridge1.PlugIn()
fridge1.cool()

print()

tv1 = TV("LG", "4K", '65"')
print("TV brand: ", tv1.brand)
print("TV Screen Quality: ", tv1.quality)
print("TV Screen Size: ", tv1.surface_area)
tv1.PlugIn()
tv1.Display()

# Hybrid

class plant:
    def __init__(self, color, height):
        self.color = color
        self.height = height
    def grow(self):
        print("Plant is growing...")

class land_plants(plant):
    def __init__(self, color, height, soil):
        self.color = color
        self.height = height
        self.soil = soil
    def landPhoto(self):
        print("Plant does photosynthesis on land.")

class water_plants(plant):
    def __init__(self, color, height, soil):
        self.color = color
        self.height = height
        self.soil = soil
    def waterPhoto(self):
        print("Plant does photsynthesis in water.")
    def waterSoilRoots(self):
        print("The plants roots are in underwater soil")

class Seaweeds(water_plants):
    def __init__(self, color, height, soil, location):
        self.color = color
        self.height = height
        self.soil = soil
        self.location = location
    def regionality(self):
        print("Seaweed is present in ", self.location, ", usually within the subtropical areas.")

class Mangroves(land_plants, water_plants):
    def __init__(self, color, height, soil, coast_location):
        self.color = color
        self.height = height
        self.soil = soil
        self.coast_location = coast_location
    def duality(self):
        print("Mangroves are on the edges of land and water, present on subtropical coastlines.")

mangrove1 = Mangroves("green", "20m", "underwater + 7pH", "Phillipines")
mangrove1.grow() # from plant class
mangrove1.landPhoto() # from land_plants class
mangrove1.waterSoilRoots() # from water_plants class
mangrove1.duality() # from Mangroves class