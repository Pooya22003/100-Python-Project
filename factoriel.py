def factorial(n):
    javab = 1
    for i in range(1, n + 1):
        javab *= i
    return javab
print(factorial(6))

#################################################

def factorial(n):
    javab = 1
    i = 1

    while i <= n:
        javab *= i
        i += 1

    return javab

print(factorial(6))

#################################################

def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n-1)
print(factoriel(5))