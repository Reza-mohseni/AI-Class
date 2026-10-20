class Character:
    def __init__(self, name, power, health, coins):
        self.name = name
        self.power = power
        self.health = health
        self.coins = coins
        self.level = 1  

    
    def show_info(self):
        print(f"{self.name} | Level: {self.level} | Power: {self.power} | Health: {self.health} | Coins: {self.coins}")

    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


    def attack(self, other):
        other.health = other.health - self.power
        print(f"{self.name} attacked {other.name}. {other.name}'s health: {other.health}")


    def earn_coins(self, amount):
        self.coins = self.coins + amount

    
    def buy_potion(self):
        if self.coins >= 20:
            self.coins = self.coins - 20
            self.health = self.health + 30
        else:
            print("Not enough coins")

    
    def level_up(self):
        self.level = self.level + 1
        self.power = self.power + 5
        print(f"{self.name} reached level {self.level}. New power: {self.power}")



a = Character("Arya", 10, 100, 50)
b = Character("Bran", 8, 80, 15)

print("--- وضعیت اولیه ---")
a.show_info()
b.show_info()

print("\n--- مبارزه ---")
a.attack(b)
b.attack(a)
a.attack(b)

print("\n--- خرید معجون و افزایش سطح ---")

a.buy_potion()


b.buy_potion()

b.level_up()

print("\n--- وضعیت نهایی ---")
a.show_info()
b.show_info()
