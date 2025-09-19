from typing import Dict
memo: Dict[int, int] = {0:0, 1:1} # store our base cases

# The Fib. Using a memoized approach.
def fib_memoized(n: int) -> int:
    if n not in memo:
        memo[n] = fib_memoized(n-1) + fib_memoized(n-2)
    return memo[n]

# This is fine. But let's automatically memoize using decorators.
# Each time our function is executed with a foreign argument,
# the decorator caches the return value.
from functools import lru_cache

# Namely, we use an LRU (Least Recently Used) cache structure.
# Here we'll specify that our cache size may grow without bound instead
# of the usual default of 128.
@lru_cache(maxsize=None)
def fib_auto_memo(n: int) -> int:
    if n < 2:
        return n
    return fib_auto_memo(n-2) + fib_auto_memo(n-1)

if __name__ == "__main__":
    # print(fib_memoized(3))
    # print(memo)
    # print(fib_memoized(6))
    # print(memo)
    print(fib_auto_memo(5))
    print(fib_auto_memo(50))