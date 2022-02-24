budget = float(input())
season  = str(input())

if budget <= 100:
    if season == "Summer":
        print(f"Economy class")
        print(f"Cabrio - {budget * 0.35 :.2f}")
    if season == "Winter":
        print(f"Economy class")
        print(f"Jeep - {budget * 0.65 :.2f}")


if 100 < budget <= 500:
    if season == "Summer":
        print(f"Compact class")
        print(f"Cabrio - {budget * 0.45 :.2f}")
    if season == "Winter":
        print(f"Compact class")
        print(f"Jeep - {budget * 0.80 :.2f}")

if budget > 500:
    if season == "Summer":
        print(f"Luxury class")
        print(f"Jeep - {budget * 0.90 :.2f}")
    if season == "Winter":
        print(f"Luxury class")
        print(f"Jeep - {budget * 0.90 :.2f}")


