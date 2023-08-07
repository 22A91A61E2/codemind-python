n=int(input())
k=n
for i in range(1,n+1):
    for j in range(1,k+1):
        print(j,end="")
    k-=1
    print()