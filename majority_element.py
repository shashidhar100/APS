# Uses python3

def get_majority_element(a):
    dic={}
    for i in range(len(a)):
        dic[a[i]]=0
    for i in range(len(a)):
        dic[a[i]]+=1
    # print(dic.values())
    for i in dic.values():
        if i>(len(a)//2):
            return 1
    else:
        return 0
    

if __name__ == '__main__':
    n=int(input())
    lis=list(map(int,input().split(" ")))
    if get_majority_element(lis):
        print(1)
    else:
        print(0)
    