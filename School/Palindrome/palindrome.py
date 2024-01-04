#User function Template for python3

class Solution:
    def is_palindrome(self, n):
        reverse = 0
        temp = n

        while temp > 0:
            r = temp % 10
            reverse = reverse * 10 + r
            temp = temp // 10 

        if reverse == n:
            return "Yes"
        else:
            return "No"



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_palindrome(n)
		print(ans)
# } Driver Code Ends