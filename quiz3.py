x = [1,2,3,4,5]
y = [2,4,3,5,6]
z = 0

for i in x:
    for j in y:
        if i == j:
            z = z+1
print(z)