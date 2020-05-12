# Uses python3
import sys

# def fibonacci_sum_naive(from_, to):
#     sum = 0

#     current = 0
#     next  = 1

#     for i in range(to + 1):
#         if i >= from_:
#             sum += current

#         current, next = next, current + next
#     # print(sum)
#     return sum % 10
def fibonacci_sum_naive(m,n):
    if n <= 1:
            return n
    f=[0]*61
    f[1]=1
    for i in range(2, 60 + 1): 
        f[i] = (f[i - 1] + f[i - 2]) % 10
    
    if n<=60 and m<=60:
        return sum(f[m:n+1])%10
    else:
        qu=n//60
        rem=n%60
        qu_m=m//60
        rem_m=m%60
        m_sum=(qu_m*sum(f[0:61])+sum(f[0:rem_m]))
        # print(m_sum,qu_m)
    
        n_sum=(qu*sum(f[0:61])+sum(f[0:rem+1]))
        # print(n_sum,qu,rem)
        return (n_sum-m_sum)%10
        
        
if __name__ == '__main__':
    # input = sys.stdin.read()
    m,n = map(int,input().split())
    print(fibonacci_sum_naive(m,n))
