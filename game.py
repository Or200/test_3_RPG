from random import randint, choice
from core.orc import Orc
from core.goblin import Goblin


class Game:

    def start(self):
        self.show_menu()


    def show_menu(cls):
        print("""
              
    1. War !!!!!
    2. exit
              
    """)
    @staticmethod
    def choose_random_monster(name):
        return choice([Orc, Goblin])(name)

    def battle(self, player, monster):
        start = False
        if not start:
            player1 , player2 = self.max_attack(player_score, monster_score, self)
            start = True
        player_score = self.roll_dice(6) + player.speed
        monster_score = self.roll_dice(6) + monster.speed
        player1.attack(player2)
        player1, player2 = player2, player1

     

    def roll_dice(self, sides):
        if sides == 6:
            return randint(1, 6)
        elif sides == 20:
            return randint(1, 20)
        else:
            print("wrong number")
            return 0

    def max_attack(self, player, monster):
        if player < monster:
            return monster, player
        else:
            return player, monster
