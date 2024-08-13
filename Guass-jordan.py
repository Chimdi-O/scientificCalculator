#matrix = [
#   [1, 1, 2, 9], 
#    [2, 4, -3, 1],
#    [3, 6, -5, 0]
#]
Height = int(input("enter the height of your array"))
Width = int(input("enter the width of your array"))
matrix = [
   [1, 1, -3, 6], 
   [2, 1, 4, 3],
   [5, 2, 16, 4]
]

current_column = 0
current_row = 0 
# guass part 
while current_column < len(matrix[0])-1: 
    for a in range(current_row,len(matrix)): 
        if matrix[a][current_column] != 0: 
            temp = matrix[a]
            matrix[a] = matrix[current_row]
            matrix[current_row] = temp
            break
    first_value  =matrix[current_row][current_column]

    for a in range(len(matrix[current_row])):
        
        matrix[current_row][a] = matrix[current_row][a]/first_value

    for a in range(current_row+1,len(matrix)):
        factor = -1 * matrix[a][current_column]/matrix[current_row][current_column]

        for b in range(len(matrix[current_row])): 
            matrix[a][b] += factor * matrix[current_row][b]

    current_column += 1 
    current_row += 1 

    
# jordan part 
current_column -= 1 
current_row -= 1 

for a in reversed(range(1,len(matrix))):
    for b in range(0,current_row): 
        factor = -1*matrix[b][current_column]
        
        for c in range(len(matrix[0])): 
            matrix[b][c] += matrix[current_row][c]*factor 
    
    current_column -= 1 
    current_row -= 1

    while matrix[current_row][current_column] != 1: 
        current_column -= 1

for i in matrix: 
    print(i)