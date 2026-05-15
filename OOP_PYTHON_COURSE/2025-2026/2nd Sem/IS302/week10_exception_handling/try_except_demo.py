try:
    number_EMIV = int(input("Enter a number: "))
    result_EMIV = 100 / number_EMIV
    print("Result:", result_EMIV)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")