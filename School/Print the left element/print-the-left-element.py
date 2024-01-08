#User function Template for python3

class Solution:
    def leftElement(self, arr, n):
        arr.sort()
        if (n%2==0):
            even=n//2
            return(arr[even-1])
        else:
            odd=n//2
            return(arr[odd])



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.leftElement(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends