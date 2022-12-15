matrix = [
    [True, 34, 5, 'School'],
    [8, 23, 20, 11, 37, 55, 17],
    ['book', 'mosh', 'arc', 'photo'],
    [-1, 'Mani']
]

for num in reversed(matrix[1]):
    if num > 1:
        for a in range(2, num):
            if (num % a) == 0:
                break
            else:
                print(num)
for a in matrix[2]:
    print(a.upper())                
