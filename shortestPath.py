#stack queue recursion and introduction
from math import inf
from queue import PriorityQueue

G = {
    'A': {
        'B': 3,
        'C': 1
    },
    'B': {
        'A': 3,
        'E': 1,
        'D': 5,
        'C': 7
    },
    'C': {
        'A': 1,
        'D': 2
    },
    'D': {
        'C': 2,
        'B': 5,
        'E': 7,
    },
    'E': {
        'B': 1,
        'D': 7
    }
}


def init(G, start):
    cost = dict()
    prev = dict()
    for vertex in G:
        cost[vertex] = inf
        prev[vertex] = ""
    cost[start] = 0
    return cost, prev


c, d = init(G, 'A')


def relax(G, u, v, cost, prev):
    if (cost[v] > cost[u] + G[u][v]):
        cost[v] = cost[u] + G[u][v]
        prev[v] = u
    return cost, prev


def DJ(G, start):
    cost, prev = init(G, start)
    visited = list()
    Q = PriorityQueue()

    for vertex in G:
        Q.put((cost[vertex], vertex))
    while (Q.empty() == False):
        c, u = Q.get()
        visited.append(u)
        for c in G[u]:
            if c not in visited:
                cost, prev = relax(G, u, c,cost, prev)
    return cost, prev

def constructPath(prev, start, end ):
    path = end
    while(prev[end] != ''):
        path= prev[end]+'->'+path
        end = prev[end]
    return path

print(DJ(G, 'A'))
cost, prev= DJ(G, 'A')
for vertex in G:
    print("Path from ", 'A', "to ", vertex, "is ", constructPath(prev, 'A', vertex))