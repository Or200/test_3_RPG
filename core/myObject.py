from random import randint, choice



class MyObject:

    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.speed = randint(5, 10)
        self.power = randint(5, 10)
        self.armor_rating = randint(5, 15)
        

    def speak(self):
        pass

    def attack(self, player2, game_instance):
        player_attack = game_instance.roll_dice(20) + self.speed
        if player_attack > player2.armor_rating:
            is_monster = False
            try:
                if self.type:
                    is_monster = True
            except:
                pass
            score = game_instance.roll_dice(6) + self.power
            if is_monster:
                if self.weapon == "knife":
                    score *= 0.5
                if self.weapon == "axe":
                    score *= 1.5
            player2.hp -= score
        else:
            pass