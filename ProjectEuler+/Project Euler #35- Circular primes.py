def sieve_of_eratosthenes(n):
    primes = [True] * n
    primes[0] = primes[1] = False

    for i in range(2, int(pow(n, 0.5) + 1)):
        if primes[i]:
            for j in range(i * i, len(primes), i):
                primes[j] = False

    return primes


def compute():
    N = int(int(input()))
    primesList = sieve_of_eratosthenes(N)

    def is_circular_prime(n):
        s = str(n)
        return all(primesList[int(s[i:] + s[:i])] for i in range(len(s)))

    ans = sum(i
              for i in range(len(primesList))
              if is_circular_prime(i)
              )
    return ans


print(compute())
