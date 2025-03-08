#User function Template for python3

class Solution:
    def lengthString(self, str):
        return len(str)
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    tcs = int(input())
    
    for _ in range(tcs):
        s=input()
        
        print(Solution().lengthString(s))
        print("~")
# } Driver Code Ends