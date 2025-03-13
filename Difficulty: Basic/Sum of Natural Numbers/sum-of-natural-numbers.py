
class Solution:
    def seriesSum(self, n : int) -> int:
        sum=0
        x=1
        while x<=n:
            sum=sum+x
            x=x+1
        return sum


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.seriesSum(n)

        print(res)
        print("~")

# } Driver Code Ends