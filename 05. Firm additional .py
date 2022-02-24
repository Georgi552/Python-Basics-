hours_needed = int(input())
day_available = int(input())
overtime_workers = int(input())
import math

days_after_trainings = day_available * 0.90
work_hours = days_after_trainings * 8
over_hours = overtime_workers * day_available * 2
total_hours = work_hours + over_hours

if math.floor(total_hours) >= hours_needed:
    print(f"Yes!{math.floor(total_hours) - hours_needed} hours left.")

if math.floor(total_hours) < hours_needed:
    print(f"Not enough time!{hours_needed - math.floor(total_hours)} hours needed.")