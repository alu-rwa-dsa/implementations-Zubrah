# define fibonacci function
def Fib(n):
    while n > 0:  # check the value to being greater than 0
        if n == 1:  # first fib number is zero
            return 0
        elif n == 2:
            return 1  # second fib is 1
        else:
            return Fib(n - 1) + Fib(n - 2)  # perform a recursion for fib function
    else:
        print("Incorrect input")


Implementation = Fib(10)
print(Implementation)
