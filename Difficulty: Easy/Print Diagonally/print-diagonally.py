#User function Template for python3

def downwardDiagonal(n, a): 
    result=[]
    for col in range(n):
        i=0
        j=col
        while i<n and j>=0:
            result.append(a[i][j])
            i+=1
            j-=1
    for row in range(1,n):
        i=row
        j=n-1
        while i<n and j>=0:
            result.append(a[i][j])
            i+=1
            j-=1
    return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDiagonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

        print("~")
# } Driver Code Ends