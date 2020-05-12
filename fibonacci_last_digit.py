# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    if n<=60:
        for _ in range(n - 1):
            previous, current = current, previous + current

        return current % 10
    else:
        f=[0]*61
        f[1]=1
        for i in range(2, 60 + 1): 
            f[i] = (f[i - 1] + f[i - 2]) % 10
        return f[n%60]
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
