#include <stdio.h>

#define max(a, b) (((a) > (b)) ? : (a) : (b))
#define min(a, b) (((a) < (b)) ? : (a) : (b))
#define N 101

typedef signed int sint32;
typedef unsigned int uint32;

typedef struct {
    sint32 x, y;
} Point;

Point start, dest;

sint32 dx[4] = {-1, 1, 0, 0};
sint32 dy[4] = {0, 0, -1, 1};

uint32 map[N][N];

void paint_edge(Point a, Point b){
    for(uint32 i = a.x; i <= b.x; i++){
        map[i][a.y] = 0;
        map[i][b.y] = 0;
    }
    for(uint32 j = a.y; j <= b.y; j++){
        map[a.x][j] = 0;
        map[b.x][j] = 0;
    }
}

void empty_inside(Point a, Point b){
    for(uint32 i = (a.x + 1); i < b.x; i++){
        for(uint32 j = (a.y + 1); j < b.y; j++){
            map[i][j] = -1;
        }
    }
}

void init_map(sint32 **rectangle, size_t rectangle_row_len, size_t rectangle_col_len){
    for(uint32 i = 0; i < N; i++)
        for(uint32 j = 0; j < N; j++)
            map[i][j] = -1;
        
    for(uint32 i = 0; i < rectangle_row_len; i++){
        Point a = {rectangle[i][0] * 2, rectangle[i][1] * 2};
        Point b = {rectangle[i][2] * 2, rectangle[i][3] * 2};
        paint_edge(a, b);
    }
    
    for(uint32 i = 0; i < rectangle_row_len; i++){
        Point a = {rectangle[i][0] * 2, rectangle[i][1] * 2};
        Point b = {rectangle[i][2] * 2, rectangle[i][3] * 2};
        empty_inside(a, b);
    }
}

void dfs(Point cur)
{
    if((cur.x == dest.x) && (cur.y == dest.y)){
        return;
    }
    
    for(uint32 i = 0; i < 4; i++){
        Point next = {cur.x + dx[i], cur.y + dy[i]};
        
        if((next.x < 0) || (next.x >= N)) continue;
        if((next.y < 0) || (next.y >= N)) continue;
        if(map[next.x][next.y] == -1) continue;
        if((map[next.x][next.y] > 0) && (map[next.x][next.y] <= (map[cur.x][cur.y] + 1))) continue;
        
        map[next.x][next.y] = (map[cur.x][cur.y] + 1);
        dfs(next);
    }
}

// rectangle_row_len은 2차원 배열 rectangle의 행(세로) 길이입니다.
// rectangle_col_len은 2차원 배열 rectangle의 열(가로) 길이입니다.
// rectangle[i][j]는 rectangle의 i번째 행의 j번째 열에 저장된 값을 의미합니다.
sint32 solution(sint32 **rectangle, size_t rectangle_row_len, size_t rectangle_col_len, sint32 characterX, sint32 characterY, sint32 itemX, sint32 itemY) 
{
    start.x = (characterX * 2);
    start.y = (characterY * 2);
    dest.x = (itemX * 2);
    dest.y = (itemY * 2);
    
    init_map(rectangle, rectangle_row_len, rectangle_col_len);
    map[start.x][start.y] = 1;
    
    /* for debug
    for(sint32 i = 20; i >= 0; i--){
        for(sint32 j = 0; j < 20; j++){
            if(map[j][i] == -1){
                printf("x ");
            }
            else{
                printf("%d ", map[j][i]);
            }
        }
        printf("\n");
    }*/
    
    dfs(start);
    
    return (map[dest.x][dest.y] / 2);
}