#User function Template for python3
class Solution:
    def isDeciBinPalin (self, N):
        l=bin(N).replace("0b","")
        s=l[::-1]
        if l==s:
            return "Yes"
        else:
            return "No"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.isDeciBinPalin(N))
# } Driver Code Ends