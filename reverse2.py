
number = int(input('Your number:'))
number_reversed = 0

while number > 0:
    digit = number % 10
    number = number // 10
    number_reversed = number_reversed * 10
    number_reversed = number_reversed + digit

print(number_reversed)