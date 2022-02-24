free_days = int(input())

work_days = 365 - free_days   #290

play_time = (work_days * 63) + (free_days * 127) # 18270 + 9525 = 27795

if play_time > 30000:
    extra_time = play_time - 30000
    play_hours = extra_time // 60
    play_mins = extra_time % 60
    print("Tom will run away")
    print(f"{play_hours} hours and {play_mins} minutes more for play")

if play_time < 30000:
    extra_time = 30000 - play_time
    play_hours = extra_time // 60
    play_mins = extra_time % 60
    print("Tom sleeps well")
    print(f"{play_hours} hours and {play_mins} minutes less for play")