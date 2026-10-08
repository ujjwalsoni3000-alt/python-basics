try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("That was not a number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("No errors!")
finally:
    print("Done.")
