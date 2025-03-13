#User function Template for python3

class Solution:
    def reverse_exponentiation(self, n):
        rev_num=int(str(n)[::-1])
        return n**rev_num

#{ 
 # Driver Code Starts
# Input handling
if __name__ == "__main__":
    T = int(input())  # test cases

    for _ in range(T):
        n = int(input())  # input N
        solution = Solution()
        ans = solution.reverse_exponentiation(n)
        print(ans)

# } Driver Code Ends