from typing import Dict
memo: Dict[int, int] = {0:0, 1:1} # store our base cases

# The Fib. Using a memoized approach.
def fib_memoized(n: int) -> int:
    if n not in memo:
        memo[n] = fib_memoized(n-1) + fib_memoized(n-2)
    return memo[n]
