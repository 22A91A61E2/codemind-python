n=int(input())
a=64+n
for i in range(n,0,-1):
    for j in range(i):
        print("%c"%(a),end=" ")
    a-=1
    print()