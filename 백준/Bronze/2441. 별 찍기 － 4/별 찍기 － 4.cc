#include <iostream>
using namespace std;

int main(){
    
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n;
    
    cin >> n;
    
    for (int s = n; s > 0; s--){
        
        for (int j = n; j > s; j--){
            cout << " ";
        }
        
        for (int i = s; i > 0; i--){
            cout << "*";
        }
    
        cout << "\n";
    }
    
    
    
    return 0;
}