# Problem 1: Return the product if it is <= 1000; otherwise, return the sum.

def calculate_result(num1, num2):
    product = num1 * num2

    if product <= 1000:
        return product
    else:
        return num1 + num2


print(calculate_result(20, 30))  # Output: 600
print(calculate_result(40, 30))  # Output: 70
