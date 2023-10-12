name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked in a week: "))
pay_rate = float(input("Enter hourly pay rate: "))
month = input("Enter month: ")
federal_rate = int(input("Enter federal tax withhoding rate: "))
state_rate = int(input("Enter state tax withhoding rate: "))

gross_pay = hours * pay_rate
federal_withholding = (federal_rate * gross_pay) /100
state_withholding = (state_rate * gross_pay) /100
total_deduction = federal_withholding + state_withholding
net_pay = gross_pay - total_deduction

print(f'''Employee Name: {name}
Hours Worked: {hours}
Pay Rate: ${pay_rate}
Gross Pay: ${gross_pay}
Deductions: 
Federal Withholding(20.0%): ${federal_withholding}
State Withholding(9.0%): ${state_withholding}
Total Deduction: ${total_deduction}
Net Pay: ${net_pay}''')


