# Uses python3
import sys

def get_optimal_value(capacity,lis):
    value = 0.
    val_uni=[lis[i][0]/lis[i][1] for i in range(len(lis))]
    val_cpy=val_uni.copy()
    val_cpy.sort(reverse=True)
    for i in range(len(lis)):
        if capacity==0:
            return value
        k=val_cpy[i]
        inx=val_uni.index(k)
        h=min(capacity,lis[inx][1])
        value+=h*k
        capacity=capacity-h
        lis[inx][1]-=h
    return value


if __name__ == "__main__":
    data = list(map(int,input().split()))
    lis=[]
    for i in range(data[0]):
        lis.append(list(map(int,input().split())))   
    opt_value = get_optimal_value(data[1],lis)

    print("{:.10f}".format(opt_value))
