#include <iostream>
using namespace std;

int main(){
    
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int value[30] = {0,};
    
    for (int i = 0; i < 28; i++){
        int search;
        cin >> search;
        
        value[search - 1] = 1;
    }
    
    for (int k = 0; k < 30; k++){
        if (value[k] == 0){
            cout << k+1 << '\n';
        }
    }
     
    return 0;
}