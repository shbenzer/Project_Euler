#include <cmath>
#include <cstdio>
#include <iostream>
using namespace std;
using std::cin;
using std::cout;
using std::endl;
using std::pow();

void subset(long int aTemp, int anIndex, int aN, int aK, long int aSet[], int& aCount) {
    if (aN < 2) {
        if(aTemp % aK == 0) {++Count; return;}
        else {return;}
    }
    
    if (anIndex == aN-1) {return;} //prevents out of bounds
    
    //at each element, we include it or skip it
    subset(aTemp,anIndex+1,aN,aK,aSet,aCount); //skip it
    aTemp += aSet[anIndex];
    subset(aTemp,anIndex+1,aN,aK,aSet,aCount);//include it
    
    if(aTemp % aK == 0) { ++aCount; cout << aTemp << endl;} //check if subset is divisible by k
}

int main() {
    /* total number of non-empty subsets in a set of size n is 2^n - 1 for complexity target*/
    
    // set up parameters
    int n = 0; // number of elements
    int k = 0; // divisor
    int count = 0; //count of non-empty subsets found

    cin >> n; //take in n from stdin
    cin >> k; //take in k from stdin
    
    long int set[n] = {}; //initialize long int array of size n
    
    for(int i = 0; i < n; ++i) { // populate subsets array 
        set[i] = pow(i+1,i+1);
    }
    

    subset(0,0,n,k,set,count);
    
    cout << count; // print :)
}
