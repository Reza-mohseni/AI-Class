class Character:
    def __init__(self, name, power, health, coins):
        self.name = name
        self.power = power
        self.health = health
        self.coins = coins
        self.level = 1  # ویژگی لول با مقدار اولیه ۱

    # متد نمایش اطلاعات
    def show_info(self):
        print(f"{self.name} | Level: {self.level} | Power: {self.power} | Health: {self.health} | Coins: {self.coins}")

    # متد زنده بودن
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    # متد حمله به کاراکتر دیگر
    def attack(self, other):
        other.health = other.health - self.power
        print(f"{self.name} attacked {other.name}. {other.name}'s health: {other.health}")

    # متد دریافت سکه
    def earn_coins(self, amount):
        self.coins = self.coins + amount

    # متد خرید معجون
    def buy_potion(self):
        if self.coins >= 20:
            self.coins = self.coins - 20
            self.health = self.health + 30
        else:
            print("Not enough coins")

    # متد لول‌آپ
    def level_up(self):
        self.level = self.level + 1
        self.power = self.power + 5
        print(f"{self.name} reached level {self.level}. New power: {self.power}")


# --- تست برنامه با متغیرهای ساده a و b ---
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
# کاراکتر a معجون می‌خرد
a.buy_potion()

# کاراکتر b سکه کافی ندارد
b.buy_potion()

# کاراکتر b یک لول بالا می‌رود
b.level_up()

print("\n--- وضعیت نهایی ---")
a.show_info()
b.show_info()
