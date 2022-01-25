def is_prime(n):
    if n == 1:
        return False
    
    limit = int(n ** 0.5) + 1
    divisor = 2

    while (divisor < limit):
        if (n % divisor == 0):
            return False
        divisor += 1

    return True

def primes_between(n,m):
    for x in range(n,m + 1):
        if is_prime(x):
            print(x)

def main():
    primes_between(3,100)

if __name__ == '__main__':
    main()
