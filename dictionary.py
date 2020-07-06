# Enter your code here. Read input from STDIN. Print output to STDOUT
# d ={}
# l=[]
# n = int(input())
# for i in range(n):
#     key,value=input().split()
#     value=int(value)
#     d[key]=value
# for a in range(len(d)):
#     a=input()
#     l.append(a)
    
# for a in l:    
#     if a in d:
#         print(a+"="+str(d[a]))
#     else:
#         print("Not found")
import sys
inputList=[]

for line in sys.stdin:
    inputList.append(line)

n = int(inputList[0])
entries = inputList[1:n+1]
queries = inputList[n+1:]

phoneBook = {}

for entry in entries:
    name, id = entry.split()
    phoneBook[name] = id

for query in queries:
    stripQuery = query.rstrip() #Eliminates the newline character
    if stripQuery in phoneBook:
        print(stripQuery + "=" + str(phoneBook[stripQuery]))
    else:
        print("Not found")
