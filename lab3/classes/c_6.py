def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

count = int(input("Enter the amount of numbers: "))
numbers = [int(input(f"Enter the number {i + 1}: ")) for i in range(count)]

primes = list(filter(is_prime, numbers))
print(primes)
