import sys

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        if not (v, w)in self.graph[u]:
            self.graph[u].append((v, w))

    def update_vertices(self):
        self.V = len(self.graph)


hotels = [i for i in range(501)]  # cost of staying at each hotel
c1 = 20
c2 = 40
c3 = 60
cost = [sys.maxint for i in range(501)]

# class hotel_graph:
#     def __init__(self, s, v, w):
#         self.src = s
#         self.dest = v
#         self.w = w

#
# hoteldata = []
# n = 0


#
# def fun_add_edge(s,n,cost):
#     if n>100:
#         return
#     hoteldata.append(hotel_graph(s,n,cost))
#     s=n
#     if n+20<=500:
#         fun_add_edge(s,n+20,hotels[n+20]+c1)
#     if n + 350 <= 500:
#         fun_add_edge(s,n+35,hotels[n+35]+c1)
#     if n + 50 <= 500:
#         fun_add_edge(s,n+50,hotels[n+50]+c1)
n = 0


def fun_add_edge_graph(n):
    if n > 500:
        return
    if n + 20 <= 500:
        hotel_data.addEdge(n, n+20, hotels[n + 20] + c1)
        fun_add_edge_graph(n+20)
    if n + 350 <= 500:
        hotel_data.addEdge(n, n + 35, hotels[n + 35] + c2)
        fun_add_edge_graph(n+35)
    if n + 50 <= 500:
        hotel_data.addEdge(n, n + 50, hotels[n + 50] + c3)
        fun_add_edge_graph(n + 50)


def find_opt(n):
    if n == 0:
        return 0
    if n == 20:
        return hotels[20] + c1
    if n == 35:
        return hotels[35] + c2
    if n == 50:
        return hotels[50] + c3
    if cost[n] != -1:
        return cost[n]
    cost[n] = min(find_opt(n - 20) + c1, find_opt(n - 35) + c2, find_opt(n - 50))
    return cost[n]


hotel_data = Graph(1)
fun_add_edge_graph(0)
print hotel_data.graph.items()
# fun_add_edge(0,0,0)
# hoteldata=hoteldata[1:]
# for data in hoteldata:
#     print data.src,data.dest,data.w
