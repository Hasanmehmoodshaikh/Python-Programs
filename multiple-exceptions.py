try:
    nr = int(input("Enter value of numerator - "))
    dr = int(input("Enter value of denominator - "))

    result = nr / dr
    print(result)

except ZeroDivisionError:    
    print("You can not divide any number by zero. Please try with other non-zero values.")

except ValueError:
    print("Invalid input value.Please provide only numbers.")