import sys
hotels = [i for i in range(501)]
c1 = 20
c2 = 40
c3 = 60
cost = [-1 for i in range(501)]


def find_opt(n):
    dist=n*5
    if dist %100!=0 or dist %175!=0 or dist %250!=0:
        return
    # if n == 20:
    #     return hotels[20] + c1
    # if n == 35:
    #     return hotels[35] + c2
    # if n == 50:
    #     return hotels[50] + c3
    if cost[n] != -1:
        return cost[n]
    n20=find_opt(n-20)
    n20+=c1
    n35 = find_opt(n - 35)
    n35 += c2
    n50 = find_opt(n - 50)
    n50 += c3
    cost[n] = min(n20,n35,n50)

    return cost[n]


print  find_opt(85)
