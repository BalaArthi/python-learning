name="Bala Arthi"
age=22
print(f"I'm {name},{age} years old")

A={1,3,5,7,9}
B={2,3,5,7}
#union using | operator
print(A|B)
#union using method
print(A.union(B))
#intersection using & operator
print(A&B)
#intersection using method
print(A.intersection(B))
#difference A-B
print(A-B)
#difference B-A
print(B-A)

Data=[10,21,32,43,54,65,76]
print(Data[::2])

names=["Alice","Bob","Charlie","David"]
names.reverse()
print(names)
names.sort()
print(names)
print(names)
print([name.upper()for name in names])

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(matrix[1][2])
print(matrix[1])
print([matrix[0][0],matrix[1][0],matrix[2][0]])

