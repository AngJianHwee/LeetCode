import collections
import itertools


def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n


def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result


def get_divisors(n):
    pf = prime_factors(n)

    pf_with_multiplicity = collections.Counter(pf)

    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in pf_with_multiplicity.items()
    ]

    for prime_power_combo in itertools.product(*powers):
        yield prod(prime_power_combo)


def solution(n):
    if n == 1:
        return "BUY"
    if n == 2:
        return "PASS"
    x = list(get_divisors(n))
    print(x)
    x = [int(x_)%2 for x_ in x]

    if sum(x) == len(x):
        return "BUY"
    elif sum(x) < len(x):
        return "PASS"
    return "SELL"


# def main():
#     n = int(input())
#     print(solution(n))


# if __name__ == "__main__":
#     main()

print(solution(2))
print(solution(100000000000))
print(solution(832483274807))
