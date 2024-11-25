
numbers_str = input("Enter a list of integers separated by commas: ")
numbers = [int(num) for num in numbers_str.split(",")]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Odd numbers:")
for num in odd_numbers:
  print(num)


class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Mango(Fruits):
    def __init__(self, name, color, variety):
        super().__init__(name, color)
        self.variety = variety
        self.color = "yellow"  # Overriding color attribute

mango = Mango("Mango", "green", "Alphonso")
print(f"Mango: {mango.name}, Color: {mango.color}, Variety: {mango.variety}")




