from .myObject import MyObject, randint, choice

class Orc(MyObject):

    def __init__(self, name):
        super().__init__(name)
        self.type = "orc"
        self.speed -= 5
        self.power += 5
        self.armor_rating = randint(2, 8)
        self.weapon = choice(["knife", "sword", "axe"])


    def speak(self):
        print(f"The {self.type} {self.name} angry!")
