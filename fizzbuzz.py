def fizz(n):
    if n % 3 == 0:
        return "Fizz"
    return str(n)

def fizz(n):
    if n % 3 == 0:
        return "Fizz"
    return str(n)

def buzz(n):
    if n % 5 == 0:
        return "Buzz"
    return str(n)

def fizz(n):
    if n % 3 == 0:
        return "Fizz"
    return str(n)

def buzz(n):
    if n % 5 == 0:
        return "Buzz"
    return str(n)

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

if __name__ == "__main__":
    fizzbuzz(20)
