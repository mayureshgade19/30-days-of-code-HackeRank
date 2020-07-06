arr =[]
T = int(input())
if (1<=T<=10):
    for i in range(T):
        S=str(input())
        arr.append(S)
    for j in arr:
        print(j[0::2],j[1::2])
