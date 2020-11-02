global dynamic

def FIBD(n):
    if n == 0 or n == 1:
        return n
    elif dynamic[n] != 0:
        return dynamic[n]
    x = FIBD(n - 2) + FIBD(n - 1)
    dynamic[n] = x
    return x

def FIB(n):
    if n == 0 or n == 1:
        return n
    return FIB(n - 2) + FIB(n - 1)


fib = int(input("fib number: "))
dynamic = [0]*fib
dynamic.insert(0, 0)
print(FIBD(fib))
print(FIB(fib))
