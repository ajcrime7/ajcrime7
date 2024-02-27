#include <stdio.h>
#include <limits.h>
#define V 5
int minDistance(int dist[], int sptSet[])
{
    int min = INT_MAX, min_index;
    for (int v = 0; v < V; v++)
        if (sptSet[v] == 0 && dist[v] <= min)
            min = dist[v], min_index = v;
    return min_index;
}
void printMST(int parent[], int graph[V][V])
{
    printf("Edge   Weight\n");
    for (int i = 1; i < V; i++)
        printf("%d - %d    %d \n", parent[i], i, graph[i][parent[i]]);
}
void primMST(int graph[V][V])
{
    int parent[V];
    int dist[V]; 
    int sptSet[V];
    for (int i = 0; i < V; i++)
        dist[i] = INT_MAX, sptSet[i] = 0;
    dist[0] = 0;
    printf("Edge   Weight\n");
    for (int count = 0; count < V - 1; count++)
    {
    
        int u = minDistance(dist, sptSet);  
        sptSet[u] = 1;
        for (int v = 0; v < V; v++)
            if (sptSet[v] == 0 && graph[u][v] && dist[u] != INT_MAX && graph[u][v] < dist[v])
                dist[v] = graph[u][v], parent[v] = u;
    }
    printMST(parent, graph);
}
int main()
{
    int graph[V][V] = {{0, 2, 0, 6, 0},
                       {2, 0, 3, 8, 5},
                       {0, 3, 0, 0, 7},
                       {6, 8, 0, 0, 9},
                       {0, 5, 7, 9, 0}};

    primMST(graph);
    return 0;
}
