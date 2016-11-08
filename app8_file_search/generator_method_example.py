# http://dabeaz.com/coroutines/
# Fibonacci numbers:
# 1, 1, 2, 3, 5, 8, 13, 21, ...


def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        nums.append(current)

    return nums

# This is the same as fib = fibonacci(100)
# for n in fib:
print('Output via lists []')
for n in fibonacci(100):
    print(n, end=', ')

print()
print()


# Co-routine example of a generator method
# A sequence, only one item at a time computed
def fibonacci_co():
    current = 0
    next = 1

    while True:
        current, next = next, next + current
        yield current


print('Output via yield instead')
for n in fibonacci_co():
    if n > 1000:
        break  # this is what stops the loop from running, no values are being stored in a list to be returned later
    print(n, end=', ')