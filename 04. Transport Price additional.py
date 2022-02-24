n = int(input())
time = str(input())

if n < 20:
    if time == "day":
        print(f"{n * 0.79 + 0.70 :.2f}")
    if time == "night":
        print(f"{n * 0.90 + 0.70 :.2f}")

elif 20 <= n < 100:
    print(f"{n * 0.09 :.2f}")

elif 100 <= n:
    print(f"{n * 0.06 :.2f}")