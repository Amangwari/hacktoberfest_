# Recursions: Recursive Vs Iterative Approach

# To find a factorial with iterative approach

# n! = n * n-1 * n-2 * n-3......1
# n! = n * (n-1)!



def factorial_iterative(n):
    """
        :parameter n: Integer
        :return: n * n-1 * n-2 * n-3........1
    """


    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac


number = int(input("Enter the number:-"))
print("Factorial Using Iterative Method", factorial_iterative(number))