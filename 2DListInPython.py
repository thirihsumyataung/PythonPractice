number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
def numInRow(lists):
    for num in lists:
        print(num)

for row in number_grid:
    for elements in row:
        print(f"{row} is item: {elements} ")
numInRow([2,3,4])