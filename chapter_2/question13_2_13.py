integer = 1000

large_exponent = int(input("Enter the exponent: "))

power = integer ** large_exponent

print(power)

# when i entered 10000 as the exponent the value error
# (ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit) displayed.
