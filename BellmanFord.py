graph=[
    [0,5,0,8],
    [5,0,2,7],
    [0,2,0,6],
    [8,7,6,0]
]

source=0
n=len(graph)
distance=[999]*n
parent=[-1]*n
visited=[0]*n
distance[source]=0

def CalculateDistance(u,v):
    if distance[v]>distance[u]+graph[u][v]:
        distance[v]=distance[u]+graph[u][v]
        parent[v]=u

def BellmanFord():
    for i in range(n-1):
        for u in range(n):
            for v in range(n):
                if graph[u][v]!=0:
                    CalculateDistance(u,v)

    for u in range(n):
        for v in range(n):
            if graph[u][v]!=0 and distance[v]>distance[u]+graph[u][v]:
                return True
    return False
    
answer=BellmanFord()
if answer=='True':
    print("Negative edges exist")
print("Negative exist doesn't exist")
