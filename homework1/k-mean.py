import math
def dis(x1,y1,x2,y2):
  return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

points = [(1,2),(3,3),(2,2),(8,8),(6,6),(7,7),(-3,-3),(-2,-4),(-7,-7)]
cluster = dict()
cluster[(-7,-7)] = []
cluster[(2,2)] = []
cluster[(-3,-3)] = []
centroid = []

for i in range(10):
    print("#"+str(i))
    print("assign step:")
    for p in points:
        mn = 100
        cl = -1
        for cen in cluster:
            if mn > dis(p[0],p[1],cen[0],cen[1]):
                mn = dis(p[0],p[1],cen[0],cen[1])
                cl = (cen[0],cen[1])
        cluster[cl].append(p)
    centroid = []
    for c in cluster:
        smx = 0
        smy = 0
        print("cluster "+ str(c)+":")
        for p in cluster[c]:
            print(p)
            smx += p[0]
            smy += p[1]
        smx /= len(cluster[c])
        smy /= len(cluster[c])
        centroid.append((smx,smy))
    #print(cluster)
    print("update step:")
    print(centroid)
    cen = [e for e in centroid]
    clus = [e for e in cluster]
    if cen == clus: break
    
    cluster = dict()
    for cen in centroid:
        cluster[cen] = []


        
