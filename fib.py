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

# Let's be even more performant. Let's use iteration!
# With this approach, our loop body will run a maximum of n-1
# times. Compare looping just 19 times compared to 21891 recursive
# calls!
def fib_iter(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        # WARNING: we use tuple unpacking here. It's clever and 
        # pithy (pythonic!) but opaque. The gist: last is 
        # set to the previous value of next, and next is set to
        # the previous value of last. We avoid the creation of 
        # a temporary variable to hold old values.
        last, next = next, last + next
    return next

if __name__ == "__main__":
    # print(fib_memoized(3))
    # print(memo)
    # print(fib_memoized(6))
    # print(memo)
    # print(fib_auto_memo(5))
    # print(fib_auto_memo(50))
    print(fib_iter(5))
    print(fib_iter(50))