#User function Template for python3
class Solution:
	def sentencePalindrome(self, s):
	    s = s.replace(" ","")
        s = s.replace(".","")
        s = s.replace(";","")
        
        a = s[::-1]
    
        if s==a:
            return 1
        else:
            return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		s = input ()
		ob = Solution()
		if ob.sentencePalindrome (s):
			print (1)
		else:
			print (0)
# } Driver Code Ends