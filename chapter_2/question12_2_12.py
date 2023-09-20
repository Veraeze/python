principal = 1000
rate_of_return = 7/100


ten_years = principal * (1 + rate_of_return) ** 10
twenty_years = principal * (1 + rate_of_return) ** 20
thirty_years = principal * (1 + rate_of_return) ** 30

print("you'll have $", round(ten_years, 2), 'deposit after 10 years')
print("you'll have $", round(twenty_years, 2), 'deposit after 20 years')
print("you'll have $", round(thirty_years, 2), 'deposit after 30 years')
