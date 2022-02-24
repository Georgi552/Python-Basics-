n_bottles = int(input())
mll = n_bottles * 750

total_dishes = 0
total_pots = 0
counter = 0
mll_needed = 0

n_dishes = input()
while n_dishes != "End":
    n_dishes = int(n_dishes)
    counter += 1
    if counter % 3 == 0:
        total_pots += n_dishes
        mll_needed += (n_dishes * 15)
    elif counter % 3 != 0:
        mll_needed += (n_dishes * 5)
        total_dishes += n_dishes
    if mll_needed > mll:
        print(f"Not enough detergent, {mll_needed - mll} ml. more necessary!")
        break
    n_dishes = input()

if n_dishes == "End":
    print(f"Detergent was enough!")
    print(f"{total_dishes} dishes and {total_pots} pots were washed.")
    print(f"Leftover detergent {mll - mll_needed} ml.")