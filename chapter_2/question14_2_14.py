age = int(input("Enter age in years: "))

max_heart_rate = 220 - age
target_heart_rate1 = (50 / 100) * max_heart_rate
target_heart_rate2 = (85 / 100) * max_heart_rate

print('your maximum heart rate is', max_heart_rate)
print('your target heart rate is within', target_heart_rate1, '-', round(target_heart_rate2, 2))