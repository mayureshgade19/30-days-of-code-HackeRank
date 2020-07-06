#import math
import os
import random
import re
import sys

def weird(n):
    if (n%2 == 0 and 2<=n<=5):
        print("Not Weird")
    elif (n%2==0 and n > 20):
        print("Not Weird")
    elif(n%2 == 0 and 6<=n<=20):
        print("Weird")
    else:
        print("Weird")
    

if __name__ == '__main__':
    N = int(input())
    weird(N)
