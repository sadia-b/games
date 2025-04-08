import random

while True:
  roll = input("Roll the dice? (y/n): ").lower()
  if roll == 'y':
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f'({dice1}, {dice2})')
  elif roll == 'n':
    print("Thanks for playing!")
    break
  else:
    print('Invalid choice!')