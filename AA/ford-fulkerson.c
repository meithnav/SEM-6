// FORD FULKERSON

#include <stdio.h>

#define MAX_NODES 10

int flow[MAX_NODES][MAX_NODES];
int capacity[MAX_NODES][MAX_NODES];
int MAX_FLOW=0;
int path[MAX_NODES+2];
int pathPointer=-1;
int n,e;



void printPath(){

    printf("     S -> ");
    for(int i=0; i<pathPointer; i++){
        printf(" %c -> ", path[i]+64);
    }

    printf(" T ");

}


void updateFlow(){

    // FIND MAX FLOW OF PATH
    int maxFLowPath = capacity[path[0]][path[1]] -flow[path[0]][path[1]] ;
    for(int i=1; i<pathPointer; i++){
        int res = capacity[path[i]][path[i+1]] -flow[path[i]][path[i+1]];
        if(maxFLowPath > res){
            maxFLowPath = res;
        }
    }

    // UPDATE MAX_FLOW
    MAX_FLOW += maxFLowPath;

    // UPDATE FLOW
    for(int i=1; i<pathPointer; i++){
        flow[path[i]][path[i+1]] += maxFLowPath; 
    }

    printf("\nPATH FLOW : %d" , maxFLowPath);

}


void findPath(int node, int goal, int visited[]){

    if(node == goal){
        updateFlow();
        printPath();
        return;
    }

    // FIND NEXT NODE
    for(int j=0; j<n; j++){

        if(visited[j]!=1 && capacity[node][j] - flow[node][j] > 0){
            visited[j]=1;
            path[++pathPointer]= j;
            findPath(j , goal, visited);
            visited[j]=0;
            pathPointer--;
        }
    }

}

void ford(int s,int goal){
    int visited[MAX_NODES+2];

    for(int i=0; i<MAX_NODES+2 ; i++){
        visited[i]=0;
        path[i]=0;
    }

    findPath(s, goal, visited);
}

int main(){

    // INITIALISE FLOW
    for(int i=0; i<MAX_NODES; i++){
        for(int j=0; j<MAX_NODES; j++){
            flow[i][j]=0;
            capacity[i][j]=0;
        }
    }

    // EDGES
    n = 6;
    e = 7;

    capacity[0][1] = 8;
    capacity[0][4] = 3;
    capacity[1][2] = 9;
    capacity[2][5] = 2;
    capacity[3][5] = 5;
    capacity[4][2] = 7;
    capacity[4][3] = 4;

    int s = 0, t = 5;
    ford(s ,t);
    printf("\n\nMAX FLOW : %d", MAX_FLOW);

    printf("\n\n");

    return 0;
}


