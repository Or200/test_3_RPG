from .myObject import MyObject, choice

class Player(MyObject):

    def __init__(self, name):
        super().__init__(name)
        self.profession = choice(["warrior", "healer"])

        if self.profession == "healer":
            self.hp += 10

        if self.profession == "warrior":
            self.power += 2

    def speak(self):
        print(f"{self.name} Ready for war and awaiting orders")









    