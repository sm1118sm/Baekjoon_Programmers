#include <iostream>
using namespace std;

int main(){
    
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n, m;
    
    cin >> n >> m;
    
    int value[100] = {0,};
    
    for (int i = 0; i < m; i++){
        int k, q, r;
        
        cin >> k >> q >> r;
        
        for (int s = k-1; s < q; s++){
            value[s] = r;
        }
    }
    
    for (int i = 0; i < n; i++){
        cout << value[i] << " ";
    }
    
    return 0;
}