import time
start_time = time.time()  # 시작 시간 기록

import numpy as np
import pandas as pd
from munkres import Munkres

def read_cost_matrix_from_csv(file_path):
    df = pd.read_csv(file_path, header=None)
    cost_matrix = df.to_numpy()
    return cost_matrix

def munkres_algorithm(cost_matrix):
    m = Munkres()
    indexes = m.compute(cost_matrix.tolist())
    total_cost = sum(cost_matrix[i][j] for i, j in indexes)
    return indexes, total_cost

def main(file_path):
    cost_matrix = read_cost_matrix_from_csv(file_path)
    indexes, total_cost = munkres_algorithm(cost_matrix)
        
    print("최적 배정:", indexes)
    print("총 최소 비용:", total_cost)

main('./Lecture_네트워크 이론과 응용_240501/HW#1_problem3_graph1.csv') # CSV 파일 경로를 여기에 입력하세요

end_time = time.time()  # 종료 시간 기록
execution_time = end_time - start_time
print("실행 시간:", execution_time, "초")