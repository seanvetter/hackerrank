

def factorial(f):
    if f <= 1:
        return f
    else:
        return f * factorial(f-1)

n = int(input())
print(factorial(n))
