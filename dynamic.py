##recusion solution


def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    return result


print(1)
print(fib(7))


def fib_dynamic(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_dynamic(n - 1, memo) + fib_dynamic(n - 2, memo)
    memo[n] = result
    return result


def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_dynamic(n, memo)


print(fib_memo(9))
