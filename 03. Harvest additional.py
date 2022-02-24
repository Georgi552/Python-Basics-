X_m2 = int(input())
Y = float(input())
Z = int(input())
Workers = int(input())
import math

grape_weight = X_m2 * Y * 0.40
liters_wine = grape_weight / 2.5

if liters_wine < Z:
    print(f"It will be a tough winter! More {math.floor(Z - liters_wine)} liters wine needed.")

if liters_wine >= Z:
    print(f"Good harvest this year! Total wine: {math.floor(liters_wine)} liters.")
    print(f"{math.ceil(liters_wine - Z)} liters left -> {math.ceil((liters_wine - Z) / Workers)} liters per person.")