def get_matrix(n,m,value):
    matrix=[]
    for i in range(n):
        result=[]
        for j in range(m):
            result.append(value)
        matrix.append(result)
    return get_matrix


result_matrix=get_matrix(2,2,10)
print(result_matrix)