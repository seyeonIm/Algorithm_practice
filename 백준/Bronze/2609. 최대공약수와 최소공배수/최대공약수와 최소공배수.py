import sys
a, b = map(int, sys.stdin.readline().rstrip().split())

def gcd(a,b):
    if (b > a):
        a,b = b,a

    while (b != 0):
        a = a%b
        a, b = b, a
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))