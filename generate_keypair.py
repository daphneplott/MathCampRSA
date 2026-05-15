import sys
from time import time
from prime_number_generation import generate_large_prime

# When trying to find a relatively prime e for (p-1) * (q-1)
# use this list of 25 primes
# If none of these work, throw an exception (and let the instructors know!)
primes = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
]


def extended_euclid(a,b,phi) -> tuple[int,int,int]:
    if b == 0:
        return (1,0,a)
    x, y, z = extended_euclid(b,a % b,phi)
    return y, (x - (a//b) * y) % phi, z

def generate_key_pairs(n_bits) -> tuple[int, int, int]:
    """
    Generate RSA public and private key pairs.
    Randomly creates a p and q (two large n-bit primes)
    Computes N = p*q
    Computes e and d such that e*d = 1 mod (p-1)(q-1)
    Return N, e, and d
    """
    p = generate_large_prime(n_bits)
    q = generate_large_prime(n_bits)
    N = p * q
    phi = (p-1)*(q-1)
    for e in primes:
        x,y,z = extended_euclid(phi,e,phi)
        if z == 1:
            break
    if y < 1:
        y += phi
    return N, e, y
