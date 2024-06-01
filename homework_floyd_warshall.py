import pandas as pd
import networkx as nx
import numpy as np

def read_graph_from_csv(file_path):
    G = nx.DiGraph()
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        source, target, weight = row
        G.add_edge(source, target, weight=float(weight))
    return G

def floyd_warshall(graph):
    nodes = list(graph.nodes)
    num_nodes = len(nodes)
    dist = np.full((num_nodes, num_nodes), float('inf'))
    pred = np.full((num_nodes, num_nodes), None)

    for i, node in enumerate(nodes):
        dist[i, i] = 0
        for neighbor in graph.neighbors(node):
            j = nodes.index(neighbor)
            dist[i, j] = graph[node][neighbor]['weight']
            pred[i, j] = node

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if dist[i, j] > dist[i, k] + dist[k, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]
                    pred[i, j] = pred[k, j]
    
    # negative cycle 감지
    for i in range(num_nodes):
        if dist[i, i] < 0:
            cycle = []
            node = nodes[i]
            while node not in cycle:
                cycle.append(node)
                node = pred[nodes.index(node)][nodes.index(node)]
            cycle.append(node)
            cycle_start = cycle.index(node)
            return cycle[cycle_start:]

    # 결과를 dict type으로 변환
    shortest_paths = {}
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j:
                shortest_paths[(nodes[i], nodes[j])] = {
                    "distance": dist[i, j],
                    "pred": pred[i, j]
                }
    
    return shortest_paths

csv_file_path = './Lecture_네트워크 이론과 응용_240501/HW#1_problem1_graph1.csv'  # CSV 파일 경로를 여기에 입력하세요
graph = read_graph_from_csv(csv_file_path)
result = floyd_warshall(graph)

if isinstance(result, dict):
    print("최단 경로:", result)
else:
    print("음의 사이클 감지:", result)
