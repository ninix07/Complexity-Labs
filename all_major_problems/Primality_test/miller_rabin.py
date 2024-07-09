import random

def miller_rabin_test(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n  == 4:
        return False

    # Write n-1 as 2^s * d
    check=n-1
    s, d = 0,0 
    while check% 2 != 1:
        s += 1
        check=check/2
    d=(n-1)//(2**s)
    if s==0:
        return False
    # Witness loop
    a = random.randint(2, n - 2)
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True

    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            break
        else:
            return False
    if x != n - 1:
            return False
    return True

if __name__=="__main__":
    if(miller_rabin_test(561)):
        print("The number is prime.")
    else:
        print("Composite number")