#User function Template for python3

class Solution:
    
     #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        bit = 2**26-1
        for i in s.lower():
            power = ord(i)-ord('a')
            if 0<=power<=25:
                bit =  bit & ~(1 << power)
        return 1 if not bit else 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        obj = Solution()
        if(obj.checkPangram(s)):
            print(1)
        else:
            print(0)
# } Driver Code Ends