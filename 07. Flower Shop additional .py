n_magnolias = int(input())
n_zumbiul = int(input())
n_roses = int(input())
n_cactuses = int(input())
gift_price = float(input())

magnolia_price = 3.25
zumbbiul_price = 4
roses_price = 3.50
cactus_price = 8
import math
EBIT = magnolia_price * n_magnolias + n_zumbiul * zumbbiul_price + n_roses * roses_price + n_cactuses * cactus_price
profit = EBIT * 0.95

if profit >= gift_price:
    print(f"She is left with {math.floor(profit - gift_price)} leva.")

else:
    print(f"She will have to borrow {math.ceil(gift_price - profit)} leva.")