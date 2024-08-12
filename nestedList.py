matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

flat_list = []
for row in matrix:
    for num in row:
        flat_list.append(num)
        
print(flat_list)