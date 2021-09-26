# Recursions: Recursive Vs Iterative Approach

# To find a factorial with Recursive approach

# n! = n * n-1 * n-2 * n-3......1
# n! = n * (n-1)!



def factorial_recursive(n):
    """
        :parameter n: Integer
        :return: n * n-1 * n-2 * n-3........1
    """

    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

number = int(input("Enter the number:-"))
print("Factorial Using recursive Method", factorial_recursive(number))

# 5 * factorial_recursive(4)
    # 5 * 4 * factorial_recursive(3)
    # 5 * 4 * 3 * factorial_recursive(2)
    # 5 * 4 * 3 * 2 * factorial_recursive(1)
    # 5 * 4 * 3 * 2 * 1 = 120