import random

class Robot:
    def __init__(self, name, attack, hp):
        self.name = name
        self.attack = attack
        self.hp = hp

    def attack_enemy(self, enemy):
        if random.random() > 0.3:
            enemy.hp -= self.attack
            print(f"{self.name} berhasil menyerang {enemy.name} dengan {self.attack} damage")
        else:
            print(f"{self.name} gagal menyerang!")
                     
    def regen_health(self):
        heal = random.randint(5, 10)
        if random.random() > 0.3:
            self.hp += heal
            if self.hp > 100:
                self.hp = 100
            print(f"{self.name} berhasil memulihkan {heal} health")
        else:
            print(f"{self.name} gagal memulihkan health")

    def give_up (self):
        self.hp = 0
        print(f"{self.name} menyerah")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} dengan hp {self.hp}"
    
class Game:
    def __init__(self, robot1, robot2, round):
        self.round = round
        self.robot1 = robot1
        self.robot2 = robot2

    def start_game(self):
        while self.robot1.is_alive() and self.robot2.is_alive():
            print(f"\nRound-{self.round}")
            print(f"{self.robot1.name} [{self.robot1.hp}]")
            print(f"{self.robot2.name} [{self.robot2.hp}]")
            
            action1 = input(f"{self.robot1.name}, pilih aksi (1. Attack 2. Regen 3. Give up): ")
            if action1 == "1":
                self.robot1.attack_enemy(self.robot2)
            elif action1 == "2":
                self.robot1.regen_health()
            elif action1 == "3":
                self.robot1.give_up()
            if not self.robot2.is_alive():
                print(f"{self.robot1.name} menang!")
                return
            
            action2 = input(f"{self.robot2.name}, pilih aksi (1. Attack 2. Regen 3. Give up): ")
            if action2 == "1":
                self.robot2.attack_enemy(self.robot1)
            elif action2 == "2":
                self.robot2.regen_health()
            elif action2 == "3":
                self.robot2.give_up()
            if not self.robot1.is_alive():
                print(f"{self.robot2.name} menang!")
                return
            
            self.round += 1
            
robot1 = Robot("Finn", random.randint(5, 15), 100)
robot2 = Robot("Ice King", random.randint(5, 15), 100)
game = Game(robot1, robot2, 1)
game.start_game()