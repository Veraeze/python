price = int(input("Enter the price: "))
credit_score = int(input("Enter credit score(press 1 for good and 0 for bad): "))
name = input("Enter name of item: ")

down_payment = 1
if credit_score == 1:
    discount = 10
elif credit_score == 0:
    discount = "There is no discount for this user"

if credit_score == 1:
    down_payment = (10 * price) / 100
elif credit_score == 0:
    down_payment = (25 * price) / 100

print(f'''          *****************************
                    Invoice
          ******************************
          Name of item: {name}
          Discount: {discount}%
          Deposit: {down_payment}''')