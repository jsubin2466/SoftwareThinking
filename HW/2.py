import random


# 랜덤 행렬 생성 함수
def make_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            value = random.randint(1, n * n * 10 - 1)
            row.append(value)
        matrix.append(row)
    return matrix


# 행렬 출력 함수
def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:4}", end="")
        print()
      
# 전치 행렬 함수
def transpose_matrix(matrix):
    n = len(matrix)
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(matrix[j][i])
        result.append(row)
    return result

# 메인 코드
n = int(input("N 입력 (2~5): "))

A = make_matrix(n)

print("원본 행렬")
print_matrix(A)

transpose = transpose_matrix(A)

print("\n전치 행렬")
print_matrix(transpose)
