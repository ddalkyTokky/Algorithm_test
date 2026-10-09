#include <string>
#include <vector>
#include <iostream>
#include <deque>

#define N 201

using namespace std;

int roads[N][N];

void init(const vector<vector<int>> fares){
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(i == j) roads[i][j] = 0; 
            else roads[i][j] = -1;
        }   
    }
    
    for(vector<int> row : fares){
        int c = row.at(0);
        int d = row.at(1);
        int f = row.at(2);
        roads[c][d] = f;
        roads[d][c] = f;
    }
}

int min_fare(int a, int b){
    if(a == -1){
        return b;
    }
    else if(b == -1){
        return a;
    }
    else{
        if(a < b){
            return a;
        }
        else{
            return b;
        }
    }
}

void floyd(int n){
    for(int k = 0; k < n+1; k++){
        for(int a = 0; a < n+1; a++){
            if(a == k) continue;
            for(int b = 0; b < n+1; b++){
                if(a == b) continue;
                if(k == b) continue;
                if((roads[a][k] != -1) && (roads[k][b] != -1)){
                    roads[a][b] = min_fare(roads[a][b], (roads[a][k] + roads[k][b]));
                }
            }
        }
    }
}

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    init(fares);
    floyd(n);
    int split_fare = (roads[s][a] + roads[s][b]);
    int cheapest_together_fare = -1;
    for(int i = 0; i < n+1; i++){
        if(s == i) continue;
        int together_fare = -1;
        if((roads[s][i] != -1) && (roads[i][a] != -1) && (roads[i][b] != -1)){
            together_fare = (roads[s][i] + roads[i][a] + roads[i][b]);
        }
        if(together_fare != -1){
            cheapest_together_fare = min_fare(cheapest_together_fare, together_fare);
        }
    }
    return min_fare(split_fare, cheapest_together_fare);
}