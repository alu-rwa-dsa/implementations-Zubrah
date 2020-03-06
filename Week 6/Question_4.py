def Matrix_Determinant_func(matrix, n):
    # temporary array for storing row
    temp_array = [0] * n
    final = 1
    determinant = 1

    # looping diagonally aligned elements
    for i in range(0, n):
        index = i
        while matrix[index][i] == 0 and index < n:
            index += 1
        # checks and confirm non zero element
        if index == n:
            continue

        # checks and confirms and loop to swaps elements
        if index is not i:
            for j in range(0, n):
                matrix[index][j], matrix[i][j] = matrix[i][j], matrix[index][j]
            determinant = determinant * int(pow(-1, index - i))

        # temporary store the swapped elements
        for j in range(0, n):
            temp_array[j] = matrix[i][j]

        # loop and transverse through lower the diagonal elements
        for j in range(i + 1, n):
            index_one = temp_array[i]  # value of diagonal element
            index_two = matrix[j][i]  # value of next row element

            # traversing every column of row
            # and multiplying to every row
            for k in range(0, n):
                matrix[j][k] = (index_one * matrix[j][k]) - (index_two * temp_array[k])

            # Det(kA)=kDet(A);
            final = final * index_one

            # multiplying the diagonal elements to get determinant
    for i in range(0, n):
        determinant = determinant * matrix[i][i]

    # Det(kA)/k=Det(A);
    return int(determinant / final)


Implementation = Matrix_Determinant_func(1, 2, 4, 6, 4,
                                         1, 3, 5, 7, 8)
