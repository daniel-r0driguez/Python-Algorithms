# GCD(a, b) = a when (b = aq + r) and r = 0.
# If r is not zero, then GCD(a, b) = GCD(r, a). Keep going until r = 0.
def GCD(a:int, b:int) -> int:
    if a == 0:
        return b
    r = b % a
    return (GCD(r, a))

def main():
    a = 1800300
    b = 10030
    print(GCD(a, b))
main()