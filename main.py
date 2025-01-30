class Warrior():
    def __init__(self, name, health, damage, stamina):
        self.name = name
        self.health = health
        self.damage = damage
        self.stamina = stamina

    def attack(self, enemy):
        enemy.health -= self.damage
        print(f"{self.name} attacks {enemy.name} for {self.damage} damage. {enemy.name}'s health is now {enemy.health}")
        self.stamina -= 10
        print(f"{self.name} uses 10 stamina. {self.name}'s stamina is now {self.stamina}")

    def rest(self):
        self.health += 10
        print(f"{self.name} heals for 10 health. {self.name}'s health is now {self.health}")
        self.stamina += 100
        print(f"{self.name} restores 100 stamina. {self.name}'s stamina is now {self.stamina}")

    def info(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Damage: {self.damage}")
        print(f"Stamina: {self.stamina}")


warrior1 = Warrior("Warrior 1", 100, 10, 100)
warrior2 = Warrior("Warrior 2", 100, 10, 100)


