# Crit efficiency calculator
import random

crit_rate_1 = float(input("crit rate: "))
crit_dmg_1 = float(input("crit dmg: "))
crit_rate_2 = float(input("\ncrit rate: "))
crit_dmg_2 = float(input("crit dmg: "))

runs = 1000000
total_damages_1 = 0.0
total_damages_2 = 0.0

def calculate_total(rate, dmg, runs=100000):
    total = 0.0
    for i in range(runs):
        r = random.random()
        if r*100 <= rate:
            total += 100+dmg
        else:
            total += 100
    return total

total_damages_1 = calculate_total(crit_rate_1, crit_dmg_1, runs=runs)
total_damages_2 = calculate_total(crit_rate_2, crit_dmg_2, runs=runs)
average_damage_1 = total_damages_1/runs
average_damage_2 = total_damages_2/runs

print(f'Average damage for first set: {average_damage_1}')
print(f'Average damage for second set: {average_damage_2}')
print(f'First set is better by {100-((average_damage_2/average_damage_1)*100)}%' \
        if average_damage_1 > average_damage_2 else \
      f'Second set is better by {100-((average_damage_1/average_damage_2)*100)}%')