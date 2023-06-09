def hamilton_Adj(v):
    O[v] = True
    global AdjArr
    global start
    global path
    path.append(v + 1)
    print(path)
    for x in range(len(AdjArr)):
        if AdjArr[v][x] == 1:
            if x == start and len(path) == len(AdjArr):
                path.append(start + 1)
                return True
            if not O[x]:
                if hamilton_Adj(x):
                    return True

    path.pop(len(path) - 1)
    O[v] = False
    return False
def hamilton_Next(v):
    O[v] = True
    global path
    global start
    global next
    path.append(v )
    for x in next[v]:
        if x == start and len(path) == len(next)-1:
            path.append(start)
            return True
        if not O[x]:
            if hamilton_Next(x):
                return True
    path.pop(len(path) - 1)
    O[v] = False
    return False

def euler_next(v):
    global path_euler
    global next
    if next[v]:             #przejscie DFS
        visited.append(v)
        z=next[v].pop(0)
        euler_next(z)
    if not next[v]:
        if visited:           #nawrót
            path_euler.append(v)
            z=visited.pop()
            euler_next(z)
    return path_euler

def iseulerian(graph):
    In = {}
    Out = {}
    for x in range(len(graph)):
        In[x]=0
    for x in range(len(graph)):
        Out[x]=len(graph[x])
        for y in graph[x]:
            In[y]+=1

    for x in range(len(graph)):
        if In[x]!=Out[x]:
            return False
    return True
def iseuladj(graph):
    deg = {}
    for x in range(len(graph)):
        deg[x]=sum(graph[x],0)

    for x in deg:
        if deg[x]%2!=0:
            return False
    return True
def euleradj(v):
    global AdjArr
    global path_euler
    global visited
    for x in range(len(AdjArr)):
        if AdjArr[v][x] == 1:
            visited.append(v)
            AdjArr[v][x] = 0
            AdjArr[x][v] = 0
            euleradj(x)
    if sum(AdjArr[v])==0:
        if visited:
            path_euler.append(v+1)
            z = visited.pop()
            euleradj(z)
    return path_euler


path = []
visited = []

print("dane z:\n"
      "1)klawiatury\n"
      "2)pliku")
abc=int(input())
if abc==1:
    print("podaj ile wierzcholkow i krawedzi")
    w, n = input().split()
    w, n = int(w), int(n)
    AdjArr = [[0 for x in range(w)] for y in range(w)]
    next = [[] for x in range(w + 1)]
    inp = []
    for x in range(n):
        inp.append(input())
    for x in inp:
        a, b = x.split()
        a, b = int(a), int(b)
        try:
            next[a].append(b)
        except:
            print('zle dane')
            quit()
    for x in inp:
        a, b = x.split()
        a, b = int(a), int(b)
        try:
            AdjArr[a - 1][b - 1] += 1
            AdjArr[b - 1][a - 1] += 1
        except:
            print("zle dane")
            quit()
else:
    f = open("dane.txt","r")
    for c in f:
        w, n = c.split()
        w, n = int(w), int(n)
        AdjArr = [[0 for x in range(w)] for y in range(w)]
        next = [[] for x in range(w + 1)]
        inp = []
        for x in range(n):
            inp.append(input())
        for x in inp:
            a, b = x.split()
            a, b = int(a), int(b)
            try:
                next[a].append(b)
            except:
                print('zle dane')
                quit()
        for x in inp:
            a, b = x.split()
            a, b = int(a), int(b)
            try:
                AdjArr[a - 1][b - 1] += 1
                AdjArr[b - 1][a - 1] += 1
            except:
                print("zle dane")
                quit()

print(next,'\n',AdjArr)
for x in range(len(AdjArr)):
    if sum(AdjArr[x]) >0:
        start = x+1
        break

O = [False for x in range(len(AdjArr)+1)]

path = []
visited = []
print("wybierz metode: \n",
      "1)hamilton \n",
      "2)euler")
co = int(input())
if co==1:
    print("wybierz reprezentacje danych:\n"
          "1)macierz sąsiedztwa\n"
          "2)lista nastepników")
    jaki=int(input())
    if jaki ==1:
        if hamilton_Adj(start):
            print(path)
        else:print("nie istenieje cykl hamiltona")
    else:
        if hamilton_Next(start):
            print(path)
        else:print("nie istenieje cykl hamiltona")
else:
    print("wybierz reprezentacje danych:\n"
          "1)macierz sąsiedztwa\n"
          "2)lista nastepników")
    jaki = int(input())
    if jaki == 1:
        if iseuladj(AdjArr):
            path_euler = []
            p = euleradj(start)
            p = p[::-1]
            p.append(start)
            print(p)
        else:print('graf nie jest eulerowski')
    else:
        if iseulerian(next):
            path_euler = []
            a = euler_next(start)
            a.append(start)
            a = a[::-1]
            print(a)
        else:print("graf nie jest eulerowski")
