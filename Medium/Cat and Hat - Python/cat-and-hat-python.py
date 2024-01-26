#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def cat_hat(str):
    count_cat = str.count("cat")
    count_hat = str.count("hat")
    if count_cat == count_hat:
        return True
    else:
        return False
  ##your code here##
  ##You need to write complete code this time 


#{ 
 # Driver Code Starts.




def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str = input()
        print(cat_hat(str))
        testcases-=1
        


if __name__=='__main__':
    main()
# } Driver Code Ends