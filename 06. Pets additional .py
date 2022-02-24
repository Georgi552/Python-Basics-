days = int(input())
food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())
import math
needed_food = days * dog_food + days * cat_food + days * turtle_food / 1000

if food >= needed_food:
    print(f"{math.floor(food - needed_food)} kilos of food left.")

if food < needed_food:
    print(f"{math.ceil(needed_food - food)} more kilos of food are needed.")