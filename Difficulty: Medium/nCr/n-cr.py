#User function Template for python3

import math
class Solution:
    def nCr(self, n, r):
        sum=1
        for i in range(1,r+1):
            sum=sum*(n-r+i)/i
        return int(sum)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = int(input())
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends