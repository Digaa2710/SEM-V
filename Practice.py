graph=[
    [0,5,0,8],
    [5,0,2,7],
    [0,2,0,6],
    [8,7,6,0]
]

n=len(graph)
source=0
distance=[999]*n
parent=[-1]*n
visited=[0]*n
distance[source]=0

def extract():
    return min((distance[i],i) for i in range(n) if not visited[i])[1]

def calculateDistance(u,v):
    if distance[v]>distance[u]+graph[u][v]:
        distance[v]=distance[u]+graph[u][v]
        parent[v]=u

def Dijikstra():
    for i in range(n):
        u=extract()
        for j in range(n):
            if graph[u][j]!=0 and visited[j]!=1:
                calculateDistance(u,j)
        visited[u]=1

Dijikstra()
print(distance)
print(parent)
