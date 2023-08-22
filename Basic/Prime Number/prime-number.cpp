//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std;

// } Driver Code Ends
class Solution{
public:
    int isPrime(int N){
        int i;
        if(N==1||N==0) 
        {
            return 0;
        }
        for(i=2;i<=sqrt(N);i++)
        {
            if(N%i==0)
            {
                return false;
            }
        }
        return true;
    }
};


//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int N;
        cin>>N;
        Solution ob;
        cout << ob.isPrime(N) << endl;
    }
    return 0; 
}
// } Driver Code Ends