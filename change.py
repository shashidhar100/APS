# Uses python3
import sys

def get_change(m):
    #write your code here
    coins=0
    qu_10=m//10
    coins+=qu_10
    m=m-(qu_10)*10
    qu_5=m//5
    coins+=qu_5
    m=m-(qu_5)*5
    coins+=m
    return coins
    
        
        
        

if __name__ == '__main__':
    # m = int(sys.stdin.read())
    m=int(input())
    print(get_change(m))
