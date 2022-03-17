print("Hello. I am the calculator.")
print("Input a calculation and I will solve it.")


def calc_input():

    repeat = True

    continue_calc = input("Do you wish to calculate something? Y/N ").strip().lower()

    if continue_calc != "y":
        repeat = False

    while repeat:
        value_1 = float(input())
        operator = input()
        value_2 = float(input())

        if operator == "+":
            print(f"{value_1} + {value_2} = {value_1 + value_2}")
        if operator == "-":
            print(f"{value_1} - {value_2} = {value_1 - value_2}")
        if operator == "/":
            print(f"{value_1} / {value_2} = {value_1 / value_2}")
        if operator == "*":
            print(f"{value_1} * {value_2} = {value_1 * value_2}")
        if operator == "**":
            print(f"{value_1} ** {value_2} = {value_1 ** value_2}")

        continue_calc = input("Do you wish to calculate something else? Y/N ").strip().lower()


calc_input()
