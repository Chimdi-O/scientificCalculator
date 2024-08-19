
#This assumes that the inputs are already in matrix form 

def solver(matrix): 
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
    xval = matrix[0][2]
    yval = matrix[1][2]
    return xval, yval
matrix = [[5,1,11], 
         [3,-1,9]]
print( solver(matrix))