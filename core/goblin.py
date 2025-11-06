from .myObject import MyObject, choice

class Goblin(MyObject):

    def __init__(self, name):
        super().__init__(name)
        self.hp = 20
        self.type = "goblin"
        self.armor_rating = 1
        self.weapon = choice(["knife", "sword", "axe"])


    def speak(self):
        print(f"The {self.type} {self.name} angry!")
