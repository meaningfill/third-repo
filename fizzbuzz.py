def fizzbuzz(n):
    """1부터 n까지의 FizzBuzz를 출력"""
    for i in range(1, n + 1):
        result = ""
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        print(result if result else i)


if __name__ == "__main__":
    fizzbuzz(20)1:
