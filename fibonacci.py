def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


n = int(input("Enter the value"))
print(fib(n))

# 0 1 1 2 3 5 8 13