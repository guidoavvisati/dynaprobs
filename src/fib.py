from typing import Dict


def fib_simple(n: int) -> int:
    if n <= 1:
        return 1
    return fib_simple(n - 1) + fib_simple(n - 2)


def fib_memo(n: int, memo: Dict = None) -> int:
    if memo is None:
        memo = {}
    if n <= 1:
        return 1
    if n in memo.keys():
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
