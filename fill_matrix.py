# fill matrix NxN with numbers in spiral
# create a matrix
# fill outer layer
# go with recursion
def fill_ring(matrix, start_x=0, start_y=0, start_value=1, n=0):
    # fill top row
    x, y, value = start_x, start_y, start_value
    while x < len(matrix) and matrix[y][x] == 0:
        matrix[y][x] = value
        x += 1
        value += 1
        n += 1
    # fill right column
    y += 1
    x -= 1
    while y < len(matrix) and matrix[y][x] == 0:
        matrix[y][x] = value
        y += 1
        value += 1
        n += 1
    # fill bottom row
    y -= 1
    x -= 1
    while x >= 0 and matrix[y][x] == 0:
        matrix[y][x] = value
        x -= 1
        value += 1
        n += 1
    # fill left column
    y -= 1
    x += 1
    while matrix[y][x] == 0:
        matrix[y][x] = value
        y -= 1
        value += 1
        n += 1

    # cycle is done
    # print(f"Cycle end. y={y}, x={x}, value={value}, n={n}")
    if n < len(matrix)**2:
        fill_ring(matrix, start_x+1, start_y+1, value, n)
    #    fill_ring(matrix, shift+1, start)

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(*matrix[i])


if __name__ == "__main__":
    size = int(input())
    # create the matrix
    mtrx = []
    for i in range(size):
        mtrx.append([0 for _ in range(size)])

    fill_ring(mtrx)
    print_matrix(mtrx)
