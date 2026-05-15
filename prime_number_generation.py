import sys
from time import time
import random


# You will need to implement this function and change the return value.
def mod_exp(x: int, y: int, N: int) -> int:
    if y == 0:
        return 1
    z = mod_exp(x, y//2, N)
    if y % 2 == 0:
        return (z**2) % N
    else:
        return (x * z**2) % N


def fermat(N: int, k: int) -> bool:
    """
    Returns True if N is prime
    """
    for i in range(k):
        a = random.randint(1, N-1)
        if a == 0:
            continue
        e = mod_exp(a,N-1,N)
        if e != 1:
            return False
    return True


def generate_large_prime(n_bits: int) -> int:
    """Generate a random prime number with the specified bit length"""

    p = random.getrandbits(n_bits)
    while not fermat(p,20):
        p = random.getrandbits(n_bits)
    return p 
