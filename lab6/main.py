import math
import copy
import networkx as nx
import matplotlib.pyplot as plt
from timeit import default_timer as timer


def graf(path, rezMatrix):  # отрисовка графа
    G = nx.DiGraph()
    M = nx.DiGraph()
    E = path
    Er = rezMatrix
    G.add_weighted_edges_from(E)
    M.add_weighted_edges_from(Er)
    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, font_weight='bold', font_color='white', node_color='black')
    nx.draw(M, pos, with_labels=True, font_weight='bold', font_color='white', node_color='red', edge_color='red')

    edge_weight = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)
    plt.show()


def mat(z, alf):  # создание списка кортеджей которая всебе хранит растоянния от вершин
    v = []
    for k in z:
        v.append(k.split())
    n = len(v)
    path = []
    for i in range(n):
        for ii in range(n):
            if v[i][ii] == "0" or v[i][ii] == '-':
                pass
            else:
                k = i
                kk = ii
                while k >= len(alf):
                    k -= len(alf)
                while kk >= len(alf):
                    kk -= len(alf)
                path.append((alf[k].upper(), alf[kk].upper(), v[i][ii]))
    return path


def read_file(f, alf):
    V = []
    z = []
    for i in f:
        z.append(i)
    path = mat(z, alf)
    for i in z:
        k = i.split()
        o = []
        for ii in k:
            if ii == "-":
                o.append(math.inf)
            else:
                o.append(int(ii))
        V.append(o)
        o = []
    return V, path


def md_get_path(path, start, end):
    result = [end]
    while end != start:
        end = path[end]
        result.append(end)
    return result[::-1]


def mod_dijkstra(matrix, start):
    dist = [matrix[start][i] for i in range(len(matrix))]
    prev = [start for i in range(len(matrix))]

    checked_nodes = set()
    checked_nodes.add(start)
    for i in range(len(matrix)):
        node = 0
        for i in range(len(matrix)):
            if dist[i] < math.inf and i not in checked_nodes:
                node = i
        if node:
            checked_nodes.add(node)
            for i in range(len(matrix)):
                if dist[i] > matrix[node][i] + dist[node]:
                    dist[i] = matrix[node][i] + dist[node]
                    prev[i] = node

    paths = []
    for i in range(len(matrix)):
        paths.append(md_get_path(prev, start, i))
    return dist, paths


def yen_path(matrix, start, end, k_max=1):
    candidates = set()
    d, p = mod_dijkstra(matrix, start)
    paths = [p[end]]
    dists = [d[end]]

    for k in range(1, k_max):
        cur_matrix = copy.deepcopy(matrix)
        for i in range(len(paths[-1]) - 1):
            node_spur = paths[-1][i]
            path_root = paths[-1][:i + 1]

            for line in paths:
                if path_root == line[:i + 1] and i + 1 < len(line):
                    cur_matrix[line[i]][line[i + 1]] = math.inf

            for node in path_root:
                if node != node_spur:
                    cur_matrix[node] = [math.inf] * len(matrix)

            d, p = mod_dijkstra(cur_matrix, node_spur)

            spur_path = p[end][1:]
            if len(spur_path) != 0:
                f_path = path_root
                for t_node in spur_path:
                    f_path.append(t_node)
                f_path = tuple(f_path)
                f_dist = 0
                for j in range(1, len(f_path)):
                    f_dist += matrix[f_path[j - 1]][f_path[j]]
                candidates.add((f_path, f_dist))

            if not len(candidates):
                break

            temp_candidates = list(candidates)
            paths.append(list(temp_candidates[0][0]))
            dists.append(temp_candidates[0][1])
            candidates.remove(temp_candidates[0])

    result = []
    for i in range(len(paths)):
        for j in range(len(paths[i])):
            paths[i][j] += 1
        if len(result) < k_max:
            result.append(paths[i])
        else:
            return result


def min_dl(mas, path, alf):
    path_m = []
    o = []
    ch = 0
    ma = math.inf
    ind = 0
    for i in mas:
        for j in range(len(i) - 1):
            for ii in path:
                if ii[0] == alf[i[j] - 1].upper() and ii[1] == alf[i[j + 1] - 1].upper():
                    path_m.append((alf[i[j] - 1].upper(), alf[i[j + 1] - 1].upper(), ii[2]))
                    ch += int(ii[2])
        o.append(path_m)
        path_m = []
        if ch < ma:
            ma = ch
            ch = 0
            ind = i
    return o, ma, ind


alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
f = open("mas.txt", "r", encoding='utf-8')
V, path = read_file(f, alf)
f.close()

n = len(V)  # число вершин в графе
s = "A"
e = "H"
start = alf.index(s.lower())  # начальная вершина
end = alf.index(e.lower())  # конечная вершина
K = 3
start_time = timer()
path_m = yen_path(V, start, end, K)
ender = timer()
print("Время построения из 8 точек:", ender - start_time, " секунд\n")

rez, mi, ind = min_dl(path_m, path, alf)
print(f'посторение пути из точки {alf[start].upper()} в тчоку {alf[end].upper()}:')
print('наименьший путь длиной:', mi)
put = ""
for ii in ind:
    put += alf[ii - 1].upper() + "->"
print(put[:-2])
graf(path, rez[path_m.index(ind)])
put = ""
for i in path_m:
    if i == ind:
        pass
    else:
        for ii in i:
            put += alf[ii - 1].upper() + "->"
        print(put[:-2])
        put = ""
        graf(path, rez[path_m.index(i)])

f = open("mas_100.txt", "r", encoding='utf-8')
V, path = read_file(f, alf)
f.close()

n = len(V)  # число вершин в графе

start_time = timer()
path_m = yen_path(V, start, end, K)
ender = timer()
print("\nВремя построения из 100 точек:", ender - start_time, " секунд")