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


# 행렬 곱셈 함수
def multiply_matrix(a, b):
    n = len(a)
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            total = 0
            for k in range(n):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)
    return result


# 행렬 덧셈 함수
def add_matrix(a, b):
    n = len(a)
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result


# 메인 코드
n = int(input("N 입력 (2~5): "))

A = make_matrix(n)
B = make_matrix(n)
C = make_matrix(n)

print("A 행렬")
print_matrix(A)

print("\nB 행렬")
print_matrix(B)

print("\nC 행렬")
print_matrix(C)

# A x B
multiplied = multiply_matrix(A, B)

# A x B + C
result = add_matrix(multiplied, C)

print("\nA x B + C 결과")
print_matrix(result)
