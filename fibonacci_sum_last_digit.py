# Uses python3
import sys

# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current

#     return sum%10

def fibonacci_sum_naive(n):
    if n <= 1:
            return n
    f=[0]*61
    f[1]=1
    for i in range(2, 60 + 1): 
        f[i] = (f[i - 1] + f[i - 2]) % 1020
    
    if n<=60:
        return sum(f[0:n+1])%10
    else:
        qu=n//60
        rem=n%60
        return (qu*sum(f[0:61])+sum(f[0:rem+1]))%10
        
        
if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(fibonacci_sum_naive(n))
