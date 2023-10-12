money = float(input("Enter amount: "))
for years in range(1, 31):
    roi = money * 0.10
    investment =  roi + money
    money = investment
    print(f'Your ROI is ${roi:.2f}, your investment is now ${investment:.2f} in year {years}')
