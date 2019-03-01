def get_summ(num_one, num_two):
    try: 
        number1 = int(num_one)
    except ValueError:
        print("It's not a number")
        return "Error"
    try:
        number2 = int(num_two)
    except ValueError:
        print("It's not a number")
        return "Error"

    return number1 + number2
new_numbers = get_summ(2, 4)
print(new_numbers)

new_numbers = get_summ("ff", "f")
print(new_numbers)
        