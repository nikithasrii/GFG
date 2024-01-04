#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (self, n):
        # code here 
        k=n%100
        k2=k%10
        k3=n//100
        k4=k//10
        m=(k2**3 + k3**3 + k4**3 )
        if m==n:
            return "Yes"
        else:
            return "No"

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends