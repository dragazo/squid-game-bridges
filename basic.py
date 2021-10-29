import sys
import math

from fractions import Fraction

memo = {}
saved = 0
def p(i: Fraction, n: Fraction) -> Fraction:
    global saved
    assert i >= 1 and n >= 0
    
    key = (i, n)
    if key in memo:
        saved += 1
        return memo[key]
    
    res = None
    if n == 0:
        return Fraction(1) # no need to cache
    elif i == 1:
        return 2 ** -n # no need to cache
    else:
        res = p(i, n - 1) / 2 + p(i - 1, n - 1) / 2

    memo[key] = res
    return res

if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} [bridge groups]', file = sys.stderr)
    sys.exit(1)

n = int(sys.argv[1])
i_m = n + 1
digits = math.floor(math.log10(i_m)) + 1
print(f'survival odds:')
for i in range(1, i_m + 1):
    frac = p(Fraction(i), Fraction(n))
    print(f'i = {i:{digits}}: {float(frac):.8f} ({frac})')

print(f'saved: {saved}')
