#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    if n==1:
        print("1")
    else:
        list1=[]
        count,ans= 0,0
        # str1=""
        while n!=1:
            list1.append(n%2)
            n=int(n/2)
        list1.append(1)
        l=list1[::-1]

        #for coverting list into string
        # for i in l:
        #     str1+=str(i)
        # print(str1)
        for i in l:
            if i == 1:
                count = count+1
                if  count > ans:
                    ans = count
            else:
                count=0
        print(ans)
