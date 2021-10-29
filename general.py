import sys
import math

from fractions import Fraction

memo = {}
saved = 0
def p(i: Fraction, n: Fraction, k: Fraction, k_0: Fraction) -> Fraction:
    global saved
    assert i >= 1 and n >= 0 and k >= 1 and k_0 >= 1
    
    key = (i, n, k, k_0)
    if key in memo:
        saved += 1
        return memo[key]
    
    res = None
    if n == 0:
        return Fraction(1) # no need to cache
    elif i == 1:
        return 1 / (k * k_0**(n - 1)) # no need to cache
    elif k == 1:
        return p(i, n - 1, k_0, k_0) # no need to cache
    else:
        res = (1 / k) * p(i, n - 1, k_0, k_0) + (1 - 1 / k) * p(i - 1, n, k - 1, k_0)

    memo[key] = res
    return res

if len(sys.argv) != 3:
    print(f'usage: {sys.argv[0]} [bridge groups] [bridges per group]', file = sys.stderr)
    sys.exit(1)

n = int(sys.argv[1])
k_0 = int(sys.argv[2])
i_m = n * (k_0 - 1) + 1
digits = math.floor(math.log10(i_m)) + 1
print(f'survival odds:')
for i in range(1, i_m + 1):
    frac = p(Fraction(i), Fraction(n), Fraction(k_0), Fraction(k_0))
    print(f'i = {i:{digits}}: {float(frac):.8f} ({frac})')

print(f'saved: {saved}')
