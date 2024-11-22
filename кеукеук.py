import random


class GameException(Exception):
   pass

class InvalidChoiceError(GameException):
   def __init__(self, message="Неправильний вибір!"):
       super().__init__(message)


class Character:
   def __init__(self, name, health, strength, defense):
       self.name = name
       self.health = health
       self.strength = strength
       self.defense = defense

   def attack(self, target):
       damage = self.strength - target.defense
       target.health = max(target.health - max(damage, 0), 0)
       print(f"{self.name} атакує {target.name} та завдає {max(damage, 0)} шкоди!")
       if target.health == 0:
           print(f"{target.name} був переможений!")

   def is_alive(self):
       return self.health > 0

   def __str__(self):
       return f"{self.name} (Здоров'я: {self.health}, Сила: {self.strength}, Захист: {self.defense})"

# Підкласи персонажів
class Warrior(Character):
   def attack(self, target):
       damage = (self.strength + 5) - target.defense
       target.health = max(target.health - max(damage, 0), 0)
       print(f"{self.name} (Воїн) завдає потужного удару {target.name} ({max(damage, 0)} шкоди)!")
       if target.health == 0:
           print(f"{target.name} був переможений!")

class Mage(Character):
   def attack(self, target):
       damage = (self.strength * 2) - target.defense
       target.health = max(target.health - max(damage, 0), 0)
       print(f"{self.name} (Маг) використовує магічний удар проти {target.name} ({max(damage, 0)} шкоди)!")
       if target.health == 0:
           print(f"{target.name} був переможений!")

class Archer(Character):
   def attack(self, target):
       critical_hit = self.strength * 1.5 if random.random() > 0.7 else self.strength
       damage = critical_hit - target.defense
       target.health = max(target.health - max(damage, 0), 0)
       print(f"{self.name} (Лучник) стріляє у {target.name} ({max(damage, 0)} шкоди)!")
       if target.health == 0:
           print(f"{target.name} був переможений!")

class Beast(Character):
   def attack(self, target):
       damage = self.strength - target.defense
       target.health = max(target.health - max(damage, 0), 0)
       self.health = min(self.health + 3, 100)  # Регенерація
       print(f"{self.name} (Чудовисько) атакує {target.name} та регенерує 3 здоров'я!")
       if target.health == 0:
           print(f"{target.name} був переможений!")

def main_menu():
   print("\nВітаємо у грі 'Бійцівський турнір'!")
   print("1. Обрати бійця")
   print("2. Почати бій")
   print("3. Переглянути результати")
   print("4. Вийти")
   choice = input("Введіть ваш вибір: ")
   return choice

def choose_character():
   print("\nДоступні персонажі:")
   print("1. Воїн")
   print("2. Маг")
   print("3. Лучник")
   print("4. Чудовисько")
   try:
       choice = int(input("Виберіть свого персонажа (1-4): "))
       if choice == 1:
           return Warrior("Воїн", 100, 20, 10)
       elif choice == 2:
           return Mage("Маг", 80, 15, 5)
       elif choice == 3:
           return Archer("Лучник", 90, 18, 8)
       elif choice == 4:
           return Beast("Чудовисько", 120, 25, 15)
       else:
           raise InvalidChoiceError()
   except ValueError:
       raise InvalidChoiceError("Введіть номер від 1 до 4!")

def start_battle(player, enemy):
   print("\nПочинається бій!")
   print(f"Ваш боєць: {player}")
   print(f"Суперник: {enemy}")
   while player.is_alive() and enemy.is_alive():
       player.attack(enemy)
       if enemy.is_alive():
           enemy.attack(player)
   if player.is_alive():
       print("\nВи перемогли!")
       return "Перемога"
   else:
       print("\nВас перемогли!")
       return "Поразка"

def main():
   results = []
   while True:
       try:
           choice = main_menu()
           if choice == "1":
               player = choose_character()
               print(f"Ви обрали: {player}")
           elif choice == "2":
               if not 'player' in locals():
                   print("Спочатку оберіть персонажа!")
                   continue
               enemy = random.choice([
                   Warrior("Воїн-Суперник", 100, 20, 10),
                   Mage("Маг-Суперник", 80, 15, 5),
                   Archer("Лучник-Суперник", 90, 18, 8),
                   Beast("Чудовисько-Суперник", 120, 25, 15)
               ])
               result = start_battle(player, enemy)
               results.append(result)
           elif choice == "3":
               print("\nРезультати боїв:")
               for i, result in enumerate(results, 1):
                   print(f"Бій {i}: {result}")
           elif choice == "4":
               print("Дякуємо за гру!")
               break
           else:
               raise InvalidChoiceError()
       except GameException as e:
           print(f"Помилка: {e}")

if __name__ == "__main__":
   main()

